
## setup (once per machine): python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
## run on command line
# python3 competitor_dash.py
## requires Python 3.11+; see requirements.txt for pinned, cross-platform-verified dependency versions

import dash
from dash import dcc, html, Input, Output, State, ctx
import dash_uploader as du
import os
import subprocess
import pandas as pd
import plotly.express as px
import numpy as np

from IPython.core.debugger import set_trace
# use set_trace()

from datetime import datetime

# Generate a unique timestamp-based folder name for uploads
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Define upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = dash.Dash(__name__)
server = app.server  # exposed for WSGI servers (e.g. gunicorn competitor_dash:server)
du.configure_upload(app, UPLOAD_FOLDER)

# Layout
app.layout = html.Div([
    html.H1("Dashboard Script Runner"),
    
    # Hidden Store to hold the timestamp
    dcc.Store(id='timestamp-store', data=timestamp),

    # Hidden Store to hold the toggle state
    dcc.Store(id='save-toggle', data=True),  # Default is True (enabled)

    # Upload Section
    html.H3("Upload a new bidder definition (Text File)"),
    du.Upload(id='upload-data',
              text='Drag and Drop or Click to Upload',
              max_files=1,
              filetypes=['txt', 'py'],
              upload_id= timestamp),
    
    html.Div(id='upload-status', style={'margin-top': '10px', 'color': 'green'}),
    
    # Run Script Button
    html.Button("Run Script", id="run-script", n_clicks=0, style={'margin-top': '20px'}),
    
    # Output Section
    html.H3("Output:"),
    html.Pre(id="output", style={"border": "1px solid black", "padding": "10px"}),

    # Plot Section
    html.H3("Auction Results Time Series"),
    dcc.Graph(id="auction-plot"),  # Add the auction-plot component here
    # html.Button("Refresh Plot", id="refresh-plot", n_clicks=0, style={'margin-top': '20px'}),

    # Button to copy and append bidder.py
    html.Button("Save Bidder File", id="save-bidder", n_clicks=0, style={'margin-top': '20px'}),
    html.Div(id="save-status", style={'margin-top': '10px', 'color': 'blue'}),
])

# Callback for file upload
@app.callback(
    Output('upload-status', 'children'),
    Input('upload-data', 'isCompleted'),
    State('upload-data', 'fileNames'),
    State('timestamp-store', 'data'),  # Pass the timestamp from the Store
    State('save-toggle', 'data'),
    prevent_initial_call=True
)
def append_to_bidder(is_completed, file_names, timestamp):
    if is_completed and file_names:
        # Generate a unique timestamp-based folder name dynamically
        
        upload_folder = os.path.join(UPLOAD_FOLDER, timestamp)
        os.makedirs(upload_folder, exist_ok=True)

        uploaded_file = os.path.join(upload_folder, file_names[0])
        bidder_file = "bidder_temp.py"
        
        with open(uploaded_file, "r") as uf, open(bidder_file, "a") as bf:
            bf.write("\n" + uf.read())
        
        return f"File '{file_names[0]}' appended to bidder_temp.py successfully."
    return "Error processing file."

# Callback for running the script and refreshing the plot
@app.callback(
    [Output("output", "children"), Output("auction-plot", "figure")],
    Input("run-script", "n_clicks"),
    prevent_initial_call=True
)
def run_script_and_update_plot(n_clicks):
    try:
        # Run the auction script
        result = subprocess.run(["python3", "run_auction.py"], capture_output=True, text=True)
        output_message = result.stdout if result.returncode == 0 else f"Error: {result.stderr}"

        # Load the auction results CSV
        csv_file = "auction_results.csv"
        if not os.path.exists(csv_file):
            return output_message, px.scatter(title="No data available")

        df = pd.read_csv(csv_file)
        df['Timestamp'] = np.array(pd.to_datetime(df['Timestamp']))

        # Create the plot
        fig = px.line(
            df,
            x="Timestamp",
            y="Total Wins",
            color="Bidder",
            hover_name="Bidder",
            title="Auction Results Over Time",
            labels={"Total Wins": "Total Wins"},
        )
        fig.update_layout(
            xaxis_title="Timestamp",
            yaxis_title="Total Wins",
            hovermode="x unified",
        )

        return output_message, fig
    except Exception as e:
        return f"Exception occurred: {str(e)}", px.scatter(title=f"Error: {str(e)}")

# # Callback to toggle the save functionality
# @app.callback(
#     Output('save-toggle', 'data'),
#     Input('toggle-save', 'n_clicks'),
#     State('save-toggle', 'data'),
#     prevent_initial_call=True
# )
# def toggle_save(n_clicks, current_state):
#     # Toggle the state (True -> False or False -> True)
#     return not current_state

# Callback to update the "Save Bidder File" button's state
@app.callback(
    Output('save-bidder', 'disabled'),
    Input('save-toggle', 'data')
)
def update_save_button_state(save_toggle_state):
    return not save_toggle_state  # Disable the button if save_toggle_state is False


# Callback to copy bidder.py and append bidder_temp.py
@app.callback(
    Output("save-status", "children"),
    Input("save-bidder", "n_clicks"),
    State('timestamp-store', 'data'),
    State('save-toggle', 'data'),
    prevent_initial_call=True
)
def save_bidder_file(n_clicks, timestamp, save_enabled):
    if not save_enabled:
        return "Save functionality is disabled."
    
    try:
        # Define file paths
        original_bidder_file = "bidder.py"
        timestamped_bidder_file = f"bidder{timestamp}.py"
        temp_bidder_file = "bidder_temp.py"

        # Make a copy of bidder.py with a timestamped name
        if os.path.exists(original_bidder_file):
            with open(original_bidder_file, "r") as original, open(timestamped_bidder_file, "w") as copy:
                copy.write(original.read())
        
        # Append the contents of bidder_temp.py to bidder.py
        if os.path.exists(temp_bidder_file):
            with open(temp_bidder_file, "r") as temp, open(original_bidder_file, "a") as original:
                original.write("\n" + temp.read())
        
        return f"Successfully saved {timestamped_bidder_file} and updated {original_bidder_file}."
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    debug = os.environ.get("DASH_DEBUG", "true").lower() == "true"
    app.run_server(host="0.0.0.0", port=port, debug=debug)
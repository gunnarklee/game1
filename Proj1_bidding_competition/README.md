# Proj1 Bidding Competition

Auction bidding simulator with a Dash-based competitor dashboard (`competitor_dash.py`) for uploading bidder scripts and running auctions.

## Requirements

- Python 3.11+
- Dependencies pinned in [requirements.txt](requirements.txt)

## 1. Local install (any machine: macOS/Linux/Windows)

```bash
# Clone or copy the repo, then from the project root:
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

Run the dashboard:

```bash
python3 competitor_dash.py
```

By default this serves on `http://0.0.0.0:8050`. Open `http://localhost:8050` in a browser.

Environment variables (optional):
- `PORT` — port to listen on (default `8050`)
- `DASH_DEBUG` — `"true"`/`"false"` to toggle Dash debug mode (default `true`)

## 2. Global (system-wide) install

If you don't want a virtual environment and want the CLI tools available globally for your user:

```bash
python3 -m pip install --user --upgrade pip
python3 -m pip install --user -r requirements.txt
python3 competitor_dash.py
```

> A virtual environment (Section 1) is still the recommended approach to avoid dependency conflicts with other projects.

## 3. Deploying to DigitalOcean App Platform

The app already exposes a WSGI `server` object (`server = app.server` in `competitor_dash.py`) and a `gunicorn` entry, so it can run as a standard Python web service.

### Steps

1. **Push this repo to GitHub/GitLab** (DigitalOcean App Platform deploys from a git repository).
2. In the DigitalOcean control panel, go to **Apps → Create App** and select this repository/branch.
3. When prompted for the resource type, choose **Web Service**.
4. Configure the build/run settings (App Platform auto-detects Python from `requirements.txt`, but verify/override):
   - **Build Command:** `pip install -r requirements.txt`
   - **Run Command:** `gunicorn --worker-tmp-dir /dev/shm --bind 0.0.0.0:$PORT competitor_dash:server`
   - **HTTP Port:** `8080` (App Platform sets `$PORT` automatically; the run command above binds to it)
5. Set any environment variables you need under **App-Level Environment Variables** (e.g. `DASH_DEBUG=false`).
6. Click **Next** through resource sizing (Basic/Starter tier is sufficient for this app) and **Create Resources**.
7. Wait for the build/deploy to finish; App Platform will give you a public URL (`https://<app-name>.ondigitalocean.app`).

### Notes for App Platform

- Do not rely on `uploads/` persisting across deploys/restarts — App Platform's filesystem is ephemeral. For durable storage of uploaded bidder files, use a DigitalOcean Space (S3-compatible) or a mounted volume instead.
- Set `debug=False` (via `DASH_DEBUG=false`) in production; Dash's debug/dev tools should not be exposed publicly.

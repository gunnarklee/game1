from users import *
from bidder import *
import os
import csv
import time
import datetime

#import Bidder_kahn

#bidder_kleemann, Bidder_kahn]

#bidder_cls= for item in 
## make each bidder named in this list, register the id that it is attached to
bidderLS = [Bidder_GAK, Bidder_Leon, Bidder_2, Bidder_3] #Bidder_Leon, Bidder_Gerry,

num_rounds = 3
num_users = 10
#num_bidders = 5

def run_auction(bidderLS, num_users, num_rounds):
    
    verbose=False
    bidders=[]
    objects={}
    
    for i in bidderLS:
        obj=i(num_users, num_rounds)
        bidders.append(obj)
        objects[id(obj)]=str(i.__name__)

    #print(bidders)
    #print(objects)
    users = [User() for _ in range(num_users)]
    auction = Auction(users, bidders, verbose=verbose)

    # Runs each auction round
    for round_number in range(num_rounds):
        if verbose:
            print('\n')
            print(f'{round_number=}')
        balances=auction.execute_round()

    # Find the key with the highest value and get the object
    winner = max(balances, key=balances.get)

    ## output outcome from the current 
    print(f'The winner is {winner} with a balance of {balances[winner]}')
    if winner in objects:
        print(f'Object name: {objects[winner]}')
    else:
        print("Object ID not found.")

    # Retrieve the result add to running score.
    result = (winner, objects, balances)

    # Append results to CSV and update running totals
    curr_time=datetime.datetime.fromtimestamp(time.time())
    
    csv_file = "auction_results.csv"
    if not os.path.exists(csv_file):
        # Create the CSV file with headers if it doesn't exist
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp","Bidder", "Wins", "Total Wins"])
            for bidder in bidderLS:
                writer.writerow([curr_time, bidder.__name__, 0, 0])
    # Read existing data
    totals = {}
    if os.path.exists(csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                totals[row["Bidder"]] = int(row["Total Wins"])

    # Update the winner's total wins
    winner_name = objects[winner]
    totals[winner_name] = totals.get(winner_name, 0) + 1

    # Write updated data back to the CSV
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow(["Timestamp", "Bidder", "Wins", "Total Wins"])
        for bidder, total_wins in totals.items():
            writer.writerow([curr_time, bidder, 1 if bidder == winner_name else 0, total_wins])

    return result

run_auction(bidderLS, num_users, num_rounds)    
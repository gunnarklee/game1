## classes 
import random

class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''
    user_ct=0
    
    def __init__(self):
        #set_trace()
        
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        self.__probability=random.uniform(0, 1)
        self.num=User.user_ct # take the next avaliable number
        User.user_ct=self.num+1 # update class wide counter
    
    def __repr__(self):
        '''User object with secret probability'''
        return (f"User object: {self.__probability}") #with secret probability: {self._prob}"

    def __str__(self):
        '''User object with a secret likelihood of clicking on an ad'''
        return (f"User object: {self.__probability}") #with secret probability: {self._prob}"

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
        draw=random.uniform(0, 1)
        if draw<=self.__probability:
            return True
        else: 
            return False
            
class Auction:
    '''Class to represent an online second-price ad auction'''
    
    def __init__(self, users, bidders, verbose=True):
        '''Initializing users, bidders, and dictionary to store balances for each bidder in the auction'''
        self.users=users
        self.bidders=bidders
        self.dictionary={}
        self.curr_round=0
        self.balances={}
        self.verbose=verbose
        if len(self.balances) == 0: 
            self.balances={id(k):0 for k in self.bidders}

    #def __repr__(self):
        '''Return auction object with users and qualified bidders'''
    #   
    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        return  [self.users, self.bidders]
    def execute_round(self):
        '''Executes a single round of an auction, completing the following steps:
            - random user selection
            - bids from every qualified bidder in the auction
            - selection of winning bidder based on maximum bid
            - selection of actual price (second-highest bid)
            - showing ad to user and finding out whether or not they click
            - notifying winning bidder of price and user outcome and updating balance
            - notifying losing bidders of price'''
        self.curr_round+=1
        user=random.choice(self.users)
        self.bid_dict= {b:b.bid(user) for b in self.bidders}
        # get the winner and update the balances
        ### find the positon and amount of the winner
        
        ## calculate winning bid and second bid amounts
        self.win_bid=sorted(self.bid_dict.values())[-1:][0]
        if len(self.bid_dict)> 1:
            self.sec_bid = sorted(self.bid_dict.values())[-2:-1][0]
        else: 
            self.sec_bid = self.win_bid

        if self.verbose:
            print(f'sec_bid:{self.sec_bid}, win_bid:{self.win_bid}, bid_dict:{self.bid_dict}') 

        for item in self.bid_dict.items():
            if item[1]==self.win_bid:
                self.winner=item[0]
                if self.verbose:
                    print(f'The winner has been identified! {self.winner}')
                    print (self.bid_dict)
                break
            else:
                #print(f'not a match for {win_bid} with {item[1]}')
                continue

        #add to the winners purse 
        self.balances[id(self.winner)]+=self.sec_bid   
        self.dictionary={self.curr_round:[user, self.bid_dict, self.balances.copy()]} #append round data to round number
        
        if self.verbose:
            print(f'New balances {self.balances}, \n from this round of bidders {self.bid_dict}')

        #showing ad to user and finding out whether or not they click
        #winner.show_ad()
        clicked=user.show_ad()
        #notifying winning bidder of price and user outcome and updating balance
        #winner.notify()
        self.winner.notify(self.winner, self.sec_bid,clicked)

        #notifying losing bidders of price
        self.winner.notify(self.winner, self.sec_bid,clicked)
        #non_winners
        #sec_bid > 
        return  self.balances
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
import auction as student_auction
import bidder as student_bidder
import numpy as np

class RefUser:
    """A representation of an internet user with a secret 
    probability of clicking on an advertisement."""
    def __init__(self, prob = None):
        if prob == None:
            self.__probability = np.random.uniform()
        else:
            self.__probability = prob

    def __repr__(self):
        return "Bandit with secret probability " + str(self.__probability)
        
    def show_ad(self):
        """ Represents showing an add to this bandit.  Returns True if bandit clicks,
        False otherwise."""
        result = np.random.choice([True, False], 
                                p = [self.__probability, 1- self.__probability])
        return result
    
class RefBidder:
    
    def __init__(self, num_users, num_rounds, fixed_bid = 1):
        self.num_users = num_users
        self.latest_bid = None
        self.fixed_bid = fixed_bid
        self.latest_auction_winner = None
        self.latest_price = None
        self.latest_clicked = None
        self.bid_called = False
        self.notify_called = False

        
    def bid(self, user_id):
        """Returns an amount of money to bid for the given user id."""
        self.bid_called = True
        return self.fixed_bid
    
    def notify(self, auction_winner, price, clicked):
        self.notify_called = True
        self.latest_auction_winner = auction_winner
        self.latest_price = price
        self.latest_clicked = clicked
        

class TestAuction(unittest.TestCase):
    def setUp(self):
        pass

    ####  USER  ####

    @weight(4)
    @visibility('visible')
    def test_construct_user(self):
        """Test User() to see if a new user can be constructed with User()."""
        try: 
            user1 = student_auction.User()
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        self.assertTrue(user1, msg='User creation did not return a User object')

    @weight(3)
    @visibility('visible')
    def test_probability_type(self):
        """Test if User has a hidden __probability with a float type."""
        try: 
            user1 = student_auction.User()
            prob_type = type(user1._User__probability)
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(prob_type == float, 
                        msg= f"Expected a probability attribute of type 'float' but observed type: {prob_type}")

    @weight(5)
    @visibility('visible')
    def test_prob_dist(self):
        """Test if User.__probability attribute is from the universal distribution (from sampling 200 User objects)"""
        try:
            result_list = []
            for _i in range(200):
                user = student_auction.User()
                result = user._User__probability
                result_list.append(result)

        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))

        max_num = max(result_list)
        min_num = min(result_list)
        avg = sum(result_list) / len(result_list)
        avg_test = avg > 0.40 and avg < 0.60

        self.assertTrue(max_num <= 1, msg=f"Maximum probability allowed should be 1 but observed: {max_num}")
        self.assertTrue(max_num <= 1, msg=f"Minimum probability allowed should be 0 but observed: {min_num}")
        self.assertTrue(avg_test, msg=f"Observed average of: {avg} is outside the expected range for the uniform distribution of 0.50 +/- 0.10")

    @weight(3)
    @visibility('visible')
    def test_show_ad(self):
        """Test if User.show_ad() returns a bool type."""
        try:
            user1 = student_auction.User()
            result = user1.show_ad()
            res_type = type(result)
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))

        self.assertTrue((res_type == bool) or (res_type == np.bool_),
                        msg=f"Expected a bool return but observed: {res_type}")
    
    @weight(5)
    @visibility('visible')
    def test_show_ad_correct_return(self):
        """Test if User.show_ad() returns the correct value based on the User.__probability (from sampling one User object 100000 times)"""
        try:
            user = student_auction.User()
            prob = user._User__probability
            result_list = []
            for _i in range(100000):
                result = user.show_ad()
                result_list.append(result)
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))

        avg = sum(result_list) / len(result_list)
        diff = round(prob,3) - round(avg, 3)
        avg_test = diff >= -0.01 and diff <= 0.01

        self.assertTrue(avg_test, msg=f"show_ad() returns: {avg} instead of the correct value based on the user probability: {prob}")
    
    ####  BIDDER  ####

    @weight(3)
    @visibility('visible')
    def test_construct_bidder_1(self):
        """Test Bidder() to see if a new bidder can be constructed with the 2 attributes: 10,10"""
        try: 
            bidder = student_bidder.Bidder(10,10)
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(bidder, msg='Bidder creation did not return a Bidder object')

    @weight(2)
    @visibility('visible')
    def test_construct_bidder_2(self):
        """Test Bidder() to see if a new bidder can be constructed with the 2 attributes: 10000, 100000"""
        try: 
            bidder = student_bidder.Bidder(10000,100000)
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(bidder, msg='Bidder creation did not return a Bidder object')

    @weight(2)
    @visibility('visible')
    def test_construct_bidder_3(self):
        """Test Bidder() to see if a new bidder can be constructed with the 2 attributes: 1000000, 5000"""
        try: 
            bidder = student_bidder.Bidder(1000000,5000)
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(bidder, msg='Bidder creation did not return a Bidder object')

    @weight(3)
    @visibility('visible')
    def test_bid_1(self):
        """Test if Bidder.bid(x) returns a non-negative amount for 100 users."""
        try: 
            bidder = student_bidder.Bidder(100,10)
            result_list = []
            for i in range(100):
                result = bidder.bid(i)
                result_list.append(result)

        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        min_res = min(result_list)

        self.assertTrue(min_res >= 0, "The lowest bid(x) returned a value of {min_res} which is not greater than or equal to zero.")
        
    @weight(4)
    @visibility('visible')
    def test_notify_1(self):
        """Test if Bidder.bid(1) followed by Bidder.notify(True, 0, True) works without error."""
        try:
            bidder = student_bidder.Bidder(10,10)
            bidder.bid(1)
            bidder.notify(True,0,True)
        
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))

        self.assertTrue(True)

    @weight(3)
    @visibility('visible')
    def test_notify_2(self):
        """Test if Bidder.bid(1) followed by Bidder.notify(False,0.1,None) works without error."""
        try:
            bidder = student_bidder.Bidder(10,10)
            bidder.bid(1)
            bidder.notify(False,0.1,None)
        
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))

        self.assertTrue(True)

    @weight(3)
    @visibility('visible')
    def test_notify_3(self):
        """Test if Bidder.bid(1) followed by Bidder.notify(True, 1.0, False) works without error."""
        try:
            bidder = student_bidder.Bidder(10,10)
            bidder.bid(1)
            bidder.notify(True, 1.0, False)

        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))

        self.assertTrue(True)

    ####  AUCTION  ####

    @weight(5)
    @visibility('visible')
    def test_construct_auction(self):
        """Test Auction() to see if a new auction can be constructed with Auction()."""
        try: 
            auction1 = student_auction.Auction([RefUser()],[RefBidder(1,10)])
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(auction1, msg='Auction creation did not return an Auction object')
 
    @weight(5)
    @visibility('visible')
    def test_execute_round(self):
        """Test if Auction.execute_round() works without error"""
        try: 
            student_auction.Auction([RefUser()],[RefBidder(1,10)]).execute_round()
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(True)
        
    @weight(5)
    @visibility('visible')
    def test_balance_at_start(self):
        """Test if a newly constructed Auction(user_list,bidder_list) has a balances attribute that is a dictionary containing zeroes"""
        try: 
            auction = student_auction.Auction([RefUser()],[RefBidder(1,10), RefBidder(1,10), RefBidder(1,10)])
            bal = auction.balances
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(len(bal)==3, "Created an Auction with 3 bidders, but balances doesn't have length 3.")
        self.assertTrue(isinstance(bal, dict)), f"auction.balances should be type: dict but is type: {type(bal)}."
        
        for key in bal:
            self.assertTrue(bal[key]==0, 
                        "Created a new Auction, but the balances attribute doesn't contain all zeroes.")
        
    @weight(5)
    @visibility('visible')
    def test_round_order(self):
        """Test if execute_round calls bid() and notify() on each bidder."""
        try: 
            bidder1, bidder2 = RefBidder(1,10), RefBidder(1,10)
            auction = student_auction.Auction([RefUser()],[bidder1, bidder2])
            auction.execute_round()
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(bidder1.bid_called, 
                        "execute_round() did not result in the first Bidder's bid method being called.")
        self.assertTrue(bidder2.bid_called, 
                        "execute_round() did not result in the second Bidder's bid method being called.")
        self.assertTrue(bidder1.notify_called, 
                        "execute_round() did not result in the first Bidder's notify method being called.")
        self.assertTrue(bidder2.notify_called, 
                        "execute_round() did not result in the second Bidder's notify method being called.")
        
    @weight(5)
    @visibility('visible')
    def test_second_price_with_click(self):
        """Test with three bidders. b0 bids 3, b1 bids 2, b2 bids 1. the user clicks. Test if auction chooses highest bidder, but with second-highest price, and check if balances are correct afterwards."""
        
        try: 
            b0, b1, b2 = RefBidder(1,10,3), RefBidder(1,10,2), RefBidder(1,10,1)
            auction = student_auction.Auction([RefUser(1)],[b0, b1, b2])
            auction.execute_round()
            bal = auction.balances
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(b0.latest_auction_winner and (not b1.latest_auction_winner) and (not b2.latest_auction_winner), 
                        "notify() argument auction_winner not set to True for b0 and False for b1 and b2.")
        self.assertTrue((round(b0.latest_price, 1) == 2) and (round(b1.latest_price, 1) == 2) and (round(b2.latest_price, 1) == 2), 
                        "notify() was not called on all bidders with the correct price (second price is 2).")
        self.assertTrue(isinstance(bal, dict)), f"auction.balances should be type: dict but is type: {type(bal)}."

        bal_list = []
        for key in bal:
            bal_list.append(bal[key])
        bal_list.sort()

        self.assertTrue(round(bal_list[0], 1) == -1, 
                        "after round, first bidder's balance not equal to -1 ($1 reward minus $2 winning price) after round.")
        self.assertTrue(round(bal_list[1], 1) == 0, 
                        "after round, second bidder's balance not equal to 0.")
        self.assertTrue(round(bal_list[2], 1) == 0, 
                        "after round, third bidder's balance not equal to 0.")

    @weight(5)
    @visibility('visible')
    def test_second_price_without_click(self):
        """Test with three bidders. b0 bids 3, b1 bids 2, b2 bids 1. the user does not click. Test if auction chooses highest bidder, but with second-highest price, and check if balances are correct afterwards."""
        
        try: 
            b0, b1, b2 = RefBidder(1,10,3), RefBidder(1,10,2), RefBidder(1,10,1)
            auction = student_auction.Auction([RefUser(0)],[b0, b1, b2])
            auction.execute_round()
            bal = auction.balances
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(b0.latest_auction_winner and (not b1.latest_auction_winner) and (not b2.latest_auction_winner), 
                        "notify() argument auction_winner not set to True for b0 and False for b1 and b2.")
        self.assertTrue((round(b0.latest_price, 1) == 2) and (round(b1.latest_price, 1) == 2) and (round(b2.latest_price, 1) == 2), 
                        "notify() was not called on all bidders with the correct price (second price is 2).")
        self.assertTrue(isinstance(bal, dict)), f"auction.balances should be type: dict but is type: {type(bal)}."

        bal_list = []
        for key in bal:
            bal_list.append(bal[key])
        bal_list.sort()

        self.assertTrue(round(bal_list[0], 1) == -2, 
                        "after round, balances[0] not equal to -2 ($0 reward minus $2 winning price) after round.")
        self.assertTrue(round(bal_list[1], 1) == 0, 
                        "after round, second bidder's balance not equal to 0.")
        self.assertTrue(round(bal_list[2], 1) == 0, 
                        "after round, third bidder's balance not equal to 0.")
        
    @weight(5)
    @visibility('visible')
    def test_click_notification_with_click(self):
        """Test with three bidders. b0 bids 3, b1 bids 2, b2 bids 1. the user clicks. Test if only the winning bidder is notified of click status."""
        
        try: 
            b0, b1, b2 = RefBidder(1,10,3), RefBidder(1,10,2), RefBidder(1,10,1)
            auction = student_auction.Auction([RefUser(1)],[b0, b1, b2])
            auction.execute_round()
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(b0.latest_auction_winner and (not b1.latest_auction_winner) and (not b2.latest_auction_winner), 
                        "notify() argument auction_winner not set to True for b0 and False for b1 and b2.")
        self.assertTrue(b0.latest_clicked, 
                        "notify() argument clicked for b0 was not True to tell b0 that the user clicked.")
        self.assertTrue((b1.latest_clicked == None) and (b2.latest_clicked == None), 
                        "notify() argument clicked not equal to None for second and third bidders.")
        
    @weight(5)
    @visibility('visible')
    def test_click_notification_without_click(self):
        """Test with three bidders. b0 bids 3, b1 bids 2, b2 bids 1. the user does not click. Test if only the winning bidder is notified of click status."""
        
        try: 
            b0, b1, b2 = RefBidder(1,10,3), RefBidder(1,10,2), RefBidder(1,10,1)
            auction = student_auction.Auction([RefUser(0)],[b0, b1, b2])
            auction.execute_round()
        except Exception as e:
            self.assertFalse(e, msg='Your program produced an exception: ' + str(e))
        
        self.assertTrue(b0.latest_auction_winner and (not b1.latest_auction_winner) and (not b2.latest_auction_winner), 
                        "notify() argument auction_winner not set to True for b0 and False for b1 and b2.")
        self.assertTrue(not b0.latest_clicked, 
                        "notify() for b0 was not False to tell b0 that the user did not click.")
        self.assertTrue((b1.latest_clicked == None) and (b2.latest_clicked == None), 
                        "notify() argument clicked not equal to None for second and third bidders.")

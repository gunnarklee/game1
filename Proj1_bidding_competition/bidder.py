import random

class Bidder_GAK:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    
    def __repr__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def __str__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def bid(self, user_id):
        '''Returns a non-negative bid amount, for some strategies user_id'''
        return random.uniform(0, 1)
        
    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        self.auction_winner =auction_winner 
        self.price =price 
        self.clicked =clicked #true/false if winner or none'
        self.round_cts += 1

class Bidder_Gerry:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    
    def __repr__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def __str__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def bid(self, user_id):
        '''Returns a non-negative bid amount, for some strategies user_id'''
        return random.uniform(0, 1)
        
    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        self.auction_winner =auction_winner 
        self.price =price 
        self.clicked =clicked #true/false if winner or none'
        self.round_cts += 1

class Bidder_Leon:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    
    def __repr__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def __str__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def bid(self, user_id):
        '''Returns a non-negative bid amount, for some strategies user_id'''
        return random.uniform(0, 1)
        
    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        self.auction_winner =auction_winner 
        self.price =price 
        self.clicked =clicked #true/false if winner or none'
        self.round_cts += 1

class Bidder_1:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    
    def __repr__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def __str__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def bid(self, user_id):
        '''Returns a non-negative bid amount, for some strategies user_id'''
        return random.uniform(0, 1)
        
    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        self.auction_winner =auction_winner 
        self.price =price 
        self.clicked =clicked #true/false if winner or none'
        self.round_cts += 1

class Bidder_2:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    
    def __repr__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def __str__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def bid(self, user_id):
        '''Returns a non-negative bid amount, for some strategies user_id'''
        return random.uniform(0, 1)
        
    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        self.auction_winner =auction_winner 
        self.price =price 
        self.clicked =clicked #true/false if winner or none'
        self.round_cts += 1

class Bidder_3:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    
    def __repr__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def __str__(self):
        '''Return Bidder object'''
        return f'Bidder(num_users={self.num_users}, num_rounds={self.num_rounds})'

    def bid(self, user_id):
        '''Returns a non-negative bid amount, for some strategies user_id'''
        return random.uniform(0, 1)
        
    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        self.auction_winner =auction_winner 
        self.price =price 
        self.clicked =clicked #true/false if winner or none'
        self.round_cts += 1        
class Bidder_2:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    def __repr__(self):
        '''Return Bidder object'''
        return(self)

    def __str__(self):
        '''Return Bidder object'''
        return(self)

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        return .5
        

    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        
        self.auction_winner=auction_winner 
        self.price =price 
        self.clicked =clicked
        self.round_cts += 1



class Bidder_3:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    def __repr__(self):
        '''Return Bidder object'''
        return(self)

    def __str__(self):
        '''Return Bidder object'''
        return(self)

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        return .5
        
class Bidder_2:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    def __repr__(self):
        '''Return Bidder object'''
        return(self)

    def __str__(self):
        '''Return Bidder object'''
        return(self)

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        return .5
        

    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        
        self.auction_winner=auction_winner 
        self.price =price 
        self.clicked =clicked
        self.round_cts += 1



class Bidder_3:
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        self.num_users =num_users
        self.num_rounds =num_rounds
        self.round_cts=0
    def __repr__(self):
        '''Return Bidder object'''
        return(self)

    def __str__(self):
        '''Return Bidder object'''
        return(self)

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        return .5
        
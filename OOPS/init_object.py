class ChaiOrder:
    
    """ self isiliy likhte hai taki usme input use kr paye or bahar 
        v hame input use krne ke liye dete hai """
        
    # creating a constructor using __init__
    
    def __init__(self,chaiType, price):
        
        """ constructor ke variable ko har jagha bina define 
        ke use kr skte hai """
        self.chaiType = chaiType
        self.price = price
        
    def summary(self):
            return f"A {self.chaiType} cup price is {self.price} rs"
        

order = ChaiOrder("cutting chai",20)

print(order.chaiType)

print(order.summary())
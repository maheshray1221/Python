# Method:01 -> code duplication

class Chai:
    def __init__(self,chaiType):
        self.chaiType = chaiType
    

"""  maine ise inherit kiya fir v isme maine variable copy kiya
isis karan ise code duplication kahte hai"""
    
class Cup(Chai):
    def __init__(self, chaiType,cup_size):
        self.chaiType = chaiType
        self.cup_size = cup_size
        
        
# Method:02 -> Explicit call

class CupTwo(Chai):
    def __init__(self, chaiType,cup_size):
       Chai.__init__(self, chaiType,cup_size)   # this is Explicit call to parant
       self.cup_size = cup_size
       
       
       
# Method:03 -> super call

class CupTwo(Chai):
    def __init__(self, chaiType,cup_size):
       super().__init__(self, chaiType)   # this is Explicit call to parant
       self.cup_size = cup_size

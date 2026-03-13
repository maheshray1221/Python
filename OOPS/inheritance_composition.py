class BaseChai:
    def __init__(self,typeChai):
        self.typeChai = typeChai
        
    def description(self):
        print(f"a {self.typeChai} chai preparing ...")
        
# inheritance

class IraniChai(BaseChai):
    
    def add_flavor(self):
        print("add suggar")
    
    
chaiOne = IraniChai("cutting")    # add input in IraniChai kyunki usne class ko inherit kiya

chaiOne.description()
chaiOne.add_flavor()
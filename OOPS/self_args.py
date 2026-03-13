""" jab kisi class ke andar koi or function define kiya jata 
hai to us function ko programming me method bolte hai"""


class ChaiCup:
    size = 200
    def describe(self):   #self argument
        return f"A {self.size} ml chai cup"
    
    
cup_one = ChaiCup()

print("before change")

print(cup_one.describe()) # calling a cup_one object

print(ChaiCup.describe(cup_one)) # calling a ChaiCup class

cup_one.size = 100


print("after change")

print(cup_one.describe()) # calling a cup_one object

print(ChaiCup.describe(cup_one)) # calling a ChaiCup class

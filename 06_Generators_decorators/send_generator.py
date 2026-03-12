def coustomer():
    print("welcome ! what  chai like you ")
   
    order = yield  # iska mtlab mujhe value send kro tabhi main aage barungaa
    while True:
        print(f"your chai is {order}")
        order = yield  # iska mtlab mujhe value send kro tabhi main aage barungaa
        
orderName = coustomer()
next(orderName)

orderName.send("ginger")


def printNumber():
    number = yield 
    while True:
        print("myNumber is",number )
        number = yield

num = printNumber()
next(num)
num.send(5)
num.send(3)
num.send(7)
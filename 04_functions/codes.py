# ---------- Function -------------

# def print_order(name,type):
#     print(f"{name} odered {type} chai")

# print_order("mahesh","Tulsi")
# print_order("jon","ilaichi")

#  multiple functions call in one function

# def hello(name):
#     print(f"hello {name}")

# def namaste(name):
#     print(f"namaste {name}")


# def greet(name):
#     hello(name)
#     namaste(name)


# greet("mahesh")    

# def calculateBill(cups,pricePerCup):
#     return cups*pricePerCup

# print(calculateBill(3,10))


#  usd to inr  

# def convert(inr,usd):
#     return inr*usd

# usdRupees = [1000,15,20]
# for usdRupee in usdRupees:
#     total_amount = convert(84,usdRupee)
#     print(f"usd to inr : {total_amount}")

# ---------  Local Scope  ---------

# def printNum():
#     a = 5       # local scope
#     print(a)

# printNum()

# ---------  Enclosing scope  ---------

# def outer():
#     c = 2
#     def inner():
#         d = 4
#         print("inner :",d)
    
#     inner()
#     print("outer : ",c)

# e = 6   # Global scope
# outer()
# print("global :",e)

# ------------   Nonlocal  ----------

# def somthing():
#     a = 10
#     def somthing2():
#         nonlocal a
#         a = 20

#     somthing2()
#     print(a)
# somthing()

# ------------   Global  ----------

# a = 10
# def somthing(): 
#     def somthing2():
#         global a
#         a = 20

#     somthing2()
#     print(a)
# somthing()
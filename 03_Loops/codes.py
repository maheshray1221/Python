# ----------  For loop  ------------------
#print 0 to 10 using range
# for i in range(7 ,10):
#     print(i ,end=" ")

# for loop with if else and break

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# else:
#     print("loop completed")

# for i in range(1,11):
#     print(f"Serving chai to Token {i}")

# orders = ["jon","tony","paul","king"]
# for order in orders:
#     print(f"Order ready for : {order}")

# ----------  enumrate ------------

# users = ["jon","tony","paul","king"]
# for idx, item in enumerate(users,start=1):
#     print(f"{idx} : {item}")

# --------------  Zip -----------------

# names = ["jon","tony","paul","king"]
# amounts = [200,150,170,100]
# z = zip(names,amounts)

# for name , amount in z:
#     print(f"{name} paid {amount} rupees")

# -------------  While  -----------------

# temp = 40
# while temp <= 100:
#     print(f"temp step : {temp}")
#     temp+=15


# ---------  Example of  walrus  -------------
# ----  Normal way --
# a = 10
# remain = a % 3
# if remain:
#     print(f"remain value : {remain}")

# ----- using Walrus (:=)  -----
# a = 10
# if remain := a%3:
#     print(f"remainder : {remain}")

size = ["small", "medium", "large"]
if (req := input("enter req = ")) in size:
    print(f"this is your {req}")
else:
    print("not availevle")
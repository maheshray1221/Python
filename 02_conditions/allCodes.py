# --------  only if  --------------
#  a = True
# if a:
#     print(" a was true")

# --------  if & else  --------------
# rahul_age = 17
# if rahul_age >= 18:
#     print("rahul you can be drive !")
# else :
#     print("rahul can not drive !")

# ----------  Voting System  -----------
# convert to int
# your_age = int(input("enter your original age .."))
# if your_age >= 18:
#     print(f"Your age {your_age} is good now you can give vote !")
# else :
#     print(f"Your age {your_age} is not setisfyed you can't give Vote !")

# ------------ if..elif..else  --------------
# type_of_cup = input("Enter type : ").lower()
# if type_of_cup == "small":
#     print("small cup cost : 10 rs. ")
# elif type_of_cup == "medium":
#     print("medium cup cost : 15 rs. ")
# elif type_of_cup == "large":
#     print("large cup cost : 20 rs. ")
# else :
#     print(f"{type_of_cup} :  type of cup size not exist !!")

# ----------  Nesting if else -------------
# device_status = "active"
# temperature = 37
# if device_status == "active":
#     print("the device is active")
#     if temperature > 35:
#         print("the temp is very high")
#     else:
#         print("tem is normal ")
# else:
#     print("device is off")

# -----------  Ternary  -------------
# cost_Amount = int(input("enter your cost Amount : "))
# delivery_charge = 0 if cost_Amount > 300 else 50
# print(f"you pay {delivery_charge} rs delivery_charge")

# ------------   match nad case -------------
seat_type = input("seat type (gernal/sleeper/Ac) => ").lower()
match seat_type:
    case "gernal":
        print("feature -> you gave Nothing")
    case "sleeper":
        print("you gave one bed")
    case "ac":
        print("you gave bed, ac, water, food, and many items")
    case _:
        print("invalid seat number")
        
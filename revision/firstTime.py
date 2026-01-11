# """import pyjokes
# print("i become a AI Devloper")
# print(pyjokes.get_joke())"""

# # all data types
# a = 3 # this is a integer variable
# b = 3.2 # this is a float variable
# c = "mahesh" # this is  a string variable
# d = True  # this is a boolean bariable
# e = None # this is a none variable


# a = 34.6 
# a = str(a)

# print(type(a))

# user detail using input -> isse user apna input likh skta hai 

# fullName = int(input("please write your good name"))
# address = input("please write your address")
# phoneNumber = int(input("please write your phone number"))

# b= fullName+phoneNumber
# b= str(b)
# print(b+address)

# print("userdetails -> ")
# print("FullName",fullName) 
# print("Address",address) 
# print("Phone Number",phoneNumber) 


# --------------->>>   STRING   <<----------------------
# slice name[start idx:end idx]  (last idx not allowed)

# Positive sliceing

# name = "tony stark"
# firstName = name[0:4]
# lastName = name[5:] 
# print(firstName)
# print(lastName)

# Negetive sliceing    (last idx not allowed)

# name = "tony stark"
# firstName = name[-10:-5]
# lastName = name[-5:] 
# print(firstName)
# print(lastName)


# Skip value  variable[str:end:skip (kitne number ka jump krna hai)]

# num = "012345678"
# print(num[1:9:2])  #   1357
# print(num[1:9:3])  #   147


#  String Method(Functions)

# len()  -----> length() 

# a = "mahesh"
# print(len(a))


# # endswith

# print(a.endswith("sh"))   # isme main puch rha hu ki mahesh ka end letter sh hai ya nhi

# # startwith

# print(a.startswith("m"))   # isme main puch rha hu ki mahesh ka end letter sh hai ya nhi

# lower/upercase

# b = "tomcroosh"
# print(b.upper())

# print(b.lower())

# strip/lstrip/rstrip (iska use space ko hatane ke liye krte hai)
# a = "  mahesh"
# b = "  mahesh  "
# c = "mahesh  "

# print(a.strip())   #remove every side space 
# print(b.lstrip())  #remove left side space
# print(c.rstrip())  #remove right side space


# swapcase (jo capital hoga bo small ho jayega or jo small hoga bo capital ho jayega)

# user = "mahesh ray "
# print(user.swapcase())

#title (iska use se har ek word ka first letter capital ho jata hai)
# print(user.title())

# f sting
# print(f"hii {user}")

# format (format ke ander value do bo value ko variable me add kr dega last me {} laga ho  (agr variable  a = "mahesh {}"))

# user = "mahesh ray {}"
# print(user.format("pro developer"))


# --------------->>>   List and Tupple   <<----------------------

# list (mutable)

# group = ["tom",34,'abc',False]
# group[0] = "jonson"
# print(group)

# List methods

# sort
# names = ["shon","tom","jon","dom"]
# names.sort()
# print(names)

# append

# fruits = ["apple", "banana"]
# number = [3.02,4.3,5,6.7,8]
# fruits.append(number)

# print(fruits)

#extend

# fruits = ["apple", "banana"]
# number = [3.02,4.3,5,6.7,8]
# fruits.extend(number)
# print(fruits)

# reverse

# fruits = ["apple", "banana"]
# fruits.reverse()
# print(fruits)

# insert

# fruits = ["apple", "banana"]
# fruits.insert(1,1000)
# print(fruits)

# #remove

# fruits.remove("apple")
# print(fruits)

# --------->> tuple <<------------

# a = ()  # this is a empty tuple
# a = (1,)  # this is a single value tuple (but need one come(,))
# a = (6,45,2,2)  # this is a one or more element tuple


# tuple methods

# count -> element kitne bar aaya hai

# b = (23,4,5,4,3,56,7,"kutta",False)
# print(type(b))   #tuple

# print(b.count(4))  #2

# index  -> element ka first index batata hai

# print(b.index(3))   #4

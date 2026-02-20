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


#  ------------>>>>  Dicsnory (Dict)  <<<----------------
# this is a mutable data type which cotain key and value pair

#  empty dicsnory

# d = {}
# print(type(d))

# marks = {
#     "rohan":89,
#     "shyam":54,
#     "toty":90,
#     "jon":96,
#     "tupple":(3,4.6,5,23,42,False,"hero")
# }


# Methods 

# 1.get()
# print(marks.get("rohan"))

# 2.keys()
# print(marks.keys())

# 3.values()
#  print(marks.values())

#  4.pop()
# print(marks.pop("rohan"))

#  add

# marks["rohan"] = 55

# 5.update({})  -> in update we use inside a obj {}
# marks.update({"tom":23,"shyam":100})

# 6. irems
# print(marks.items())

# .7 len

# print(len(marks))

# print(marks.keys())


#  ------------>>>>  Sets   <<<----------------
#  set is a well defind collection of unique element its unodered

# empyt set
# e = set()
# print(type(e))

# s = {34,63,"rohan","virat",True}  #value contain set

# print(type(s))

# methods
# 01. add()
# p = {3,4,5,6,7}
# p.add("hardik")
# print(p)

# 02. update([])  -> in update we use a inside a array []
# set me update method use krne se value update nhi balki multiple value front me add hota hai

# u = {"sriyas","kurnal","kl rahul"}
# u.update(["jassi","mia magic"])
# print(u)

# 03. remove(ele)

# r = {1,2,3,4,5,6,7,8,9}
# r.remove(5)  # {1,2,3,4,6,7,8,9}
# r.remove(10) # error
# print(r) 

# 04. discard(ele) -> ye method element ko remove krta hai agar element exist nhi krta to error nhi balki none deta hai

# d = {1,2,3,4,5} 
# print(d.discard(6)) # none
# print(d.discard(2))  # print none hoga lekin set se value remove ho jayega
# print(d)
 
# 05. pop() -> delete random element 

# p = {2,3,4,5,6}
# print(p.pop()) #2
# print(p.pop()) #3
# print(p.pop()) #4

# 06. clear() -> set become empty

# p = {2,3,4,5,6,7}
# print(p) # alll value
# p.clear()
# print(p)  # empty set

# ---------->>>  MOST IMPORTANT METHODS <<<-------    
# 01. union() or | ->> only unique element

# a = {2,3,4,7}
# b = {2,3,6,5}

# print(a|b)  # {2,3,4,7,6,5}

# 02. intersection() or &  ->> only common element

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a&b) #{3,4}

# 03. difference() or -  ->>>  left ka bo element jo right me nhi hai

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a-b) #{1,2}

#  # 04. symmetric_difference() or ^  ->>> common element hata ke

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a^b) #{1,2,5,6}



# conditions in python

# example of if statement

# age = int(input("enter your age: "))
# if(age>=18):
#     print("you can give vote")
#     print("choose your prime minister")
    

# example of if else statement

# age = int(input("enter your age: "))
# if(age>=18):
#     print("you can give vote")
#     print("choose your prime minister")
# else:
#     print("you can't give vote")
#     print("please go back your home")
    
# example of if elif else statement

# age = int(input("enter your age: "))

# if(age>18):
#     print("you can drive")
# elif(age>=18):   
#     print("you can drive but please get permisions your parant")    
# else:
#     print("pheli fursat me nikkal chotu")

# Nested if statement

# age = 30
# id_Pass = True

# if(age>18):
#     if(id_Pass):
#         print("you can visit the show")

# else:
#     print("you can't visit show")

# use logical operator -> and, or, not

# age = 20 
# gender = "femal"

# if(age > 18) and (gender == "male"):
#     print("you can visit ouer shop")

# else:
#     print("no no can't visit")

# member ship operator in , not in
list_a = [5,4,32,3,4,5]

# if(32 in list_a):
#     print("this is exist")

# else:
#     print("nhi hai hamre pass")
# ------------------
# if(32 not in list_a):
#     print("nhi hai hamre pass")

# else:
#     print("this is exist")

# age = 20

# typeofHuman = "adult" if age>18 else"minor"

# print(typeofHuman)


# questions practice
# 01. find gretest number

# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# num3 = int(input("enter third number"))
# num4 = int(input("enter fourth number"))

# if(num1>num2 and num1>num3 and num1>num4):
#     print("gratest number 1st = ",num1)
    
# elif(num2>num3 and num2>num4):
#     print("gratest number 2nd = ",num2)
    
# elif(num3>num4):
#     print("gratest number 3rd = ",num3)
    
# else:
#     print("gratest number 4th = ",num4)

# 02. user pass or fail

# sub1 = int(input("enter 1st subject marks"))
# sub2 = int(input("enter 2nd subject marks"))
# sub3 = int(input("enter 3rd subject marks"))

# total_Percentage = (100*(sub1+sub2+sub3))/300
# if(total_Percentage > 33 and sub1>33 and sub2>33 and sub3>33):
#     print("User are pass")
    
# else:
#     print("User are fail")

# 03. detect spam comment


# p1 = "make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# comment = input("enter a comment..")

# if ((p1 in comment)or (p2 in comment) or (p3 in comment)or (p4 in comment)):
#     print("this is a spam comment")
# else:
#     print("this is a genuan message")


# 04. find a given username less then 10 characters

# username = input("Enter your username. ")

# if (len(username) < 10):
#     print("this is valid Username")
    
# else:
#     print("this is Invalid Username")


# 05. find a name is given in a list

# list = ["mahesh","jon","shon","tom","tokiyo"]

# name = input("enter name.. ")

# if(name in list):
#     print("this name is exist")
    
# else:
#     print("this name is not exist")

# 06. give grade for user marks

# marks = int(input("Enter your marks out of 100 / "))

# if (marks >= 90 and marks <=100):
#     print("Execlent")
# elif(marks >= 80 and marks <=90):
#     print("A Grade")
# elif(marks >= 70 and marks <=80):
#     print("B Grade")
# elif(marks >= 60 and marks <=70):
#     print("C Grade")
# elif(marks >= 50 and marks <=60):
#     print("D Grade")
# else:
#     print("fail")

# 07. detect name in a post

# name = "Harry"

# post = input("enter post.. ")

# if(name in post):
#     print("this name is exist")

# else:
#     print("this name is not exist")



#  chepter 7 Loops-------------->>

# -------==>>  for loop

# items = ["chin","volet","wouch","belt","pent","shirt"]

# for saman in items:
#     print(saman ,end=" ")

# print 1 to 100

# range(starting index , ending index)

# for i in range(5,101):
#     print(i,end=" ")

# -------==>>  while loop

# count = 0
# while count<10:
#     print(count)
#     count += 1


# for i in range(5):
#     if(i == 2):
#         continue    
#     print(i)   #output = 0 1 3 4

# use pass 

# for i in range(5):
#     if i == 2:
#         pass
    # print(i)  #output = 0 1 2 3 4


# 01. write a table given by user

# num = int(input("enter a number where you want to show table"))

# for i in range(1,11):
#     print(num*i)
    

# 02. greet all the person in a list

# l = ["Harry","Potter","Tatty","Potty"]

# for name in l:
#     print("hello ",name)


# 03. white table using while loop

# num = int(input("enter a number where you want to show table"))
# i = 1
# while (i<=10):
#     print(num*i)
#     i+=1



# ---------->>>   Function and Recursion

# functin defination
# def greet ():
#     print("hello every one")
    
# # function call
# greet()

# # argument pass in function
# def namste(sirname,name="mahehs"):
#     print("namste",name)
#     print(sirname)
    
# namste("hero")


# Factorial using requrtion

# fact(n) = n * fact(n-1)

# def factorial(n):
#     # base case
#     if(n == 0 or n == 1):
#         return 1
#     # call itself
#     return n * factorial(n-1)

# n = int(input("enter a number : "))

# print(f"factorial of {n} :",factorial(n))


# function practice questions

# 01. find gretest number 

# def gretest(n1,n2,n3):
#     if((n1>n2)and(n1>n3)):
#         print("gretest number is :",n1)
#     elif(n2>n3):
#         print("gretest number is :",n2)
#     else:
#         print("gretest number in :",n3)


# n1 = int(input("enter number"))
# n2 = int(input("enter number"))
# n3 = int(input("enter number"))
# gretest(n1,n2,n3)


# 02. conver celsius to fahrenheit

# 1 celsius = 33.8 f

# def convert_CtoF(cels):
#     return cels*33.8

# temp = int(input("enter tempreture in celsius"))

# result = convert_CtoF(temp)

# print(result,"F")

# 03.
# print("hero\n")


# 1 to 5
# 1+2+3+4+5 = 15
# sum(5)
# 5+sum(4)
# 5+4+sum(3)
# 5+4+3+sum(2)
# 5+4+3+2+sum(1) = 1+2+3+4+5 = 15 ans
#04. sum of fist n natural number using recursion

# def sumOFn(n):
#     if(n == 1):
#         return 1
#     return n+sumOFn(n-1)

# print(sumOFn(5))

# print this
# ***
# **
# *

# def pattern(n):
#     if n == 0:
#         return
        
#     print("*"*n)
#     pattern(n-1)
        
        
# pattern(3)

# =================  Snake water gun game  =====================

# 1 = Snake	Water	Snake wins (snake drinks water)
# 2 = Water	Gun	Water wins (gun sinks in water)
# 3 = Gun	Snake	Gun wins (gun kills snake)

import random
computer = random.randint(1,3)  #snake
youstr = input("enter Character in this 'S' 'W' 'G' ")
youDic = {'S':1,'W':2,'G':3}
you = youDic[youstr]

if(computer == 2 and you == 1):
    print("You Win!")
elif(computer == 2 and you == 3):
    print("You Loss!")
elif(computer == 1 and you == 2):
    print("You Loss!")
elif(computer == 1 and you == 3):
    print("You Win!")
elif(computer == 3 and you == 2):
    print("You Win!")
elif(computer == 3 and you == 1):
    print("You Loss!")
else:
    print("Draw")
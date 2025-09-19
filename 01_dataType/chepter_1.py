# -------------  immutable  ------------------
# count = 1
# print(f"hello count : {count}")
# count = 5
# print(f"namaste count : {count}")
# print(f"identity 1 : {id(1)}")
# print(f"identity 5 : {id(5)}")


# ----------------  Mutable  ------------------

# a = set()
# print(f"id of a :{id(a)}")
# a.add("hero")
# a  .add("kalu")
# print(f"id of a : {id(a)}")

# --------------- Number ----------------
# adding
# a = 2
# b = 4
# print(f"result of adding : {a+b}")
# #Subtact
# c = 8
# d = 3
# #multiple
# print(f"multiple of this : {c*d}")
# # power
# print(f"power of this : {b**a}")

# print(f"subtract of this : {c-d}")
# #devid
# print(f"devid of this : {c/d}")
# #double devid
# print(f"double devid of this : {c//d}")
# #remender - module
# print(f"module of this : {c%d}")

#--------------- Boolean --------------
# a = 1
# b = True
# c = 0  # 0,nane
# result = a+b
# print(f"add : {result}")
# #bool
# print(f"type of :{bool(a)}")
# print(f"type of :{bool(c)}")

#-------------- logical operator -------------

# a = True
# b = False
# print(f"result : {a and b}") #false
# print(f"result : {a or b}") #true

#--------------  sys ----------

# import sys
# print(sys.float_info)

#--------------  String  -----------
# first_name = "Mahesh"
# last_name = "Ray"
# full_name = first_name+last_name
# print(f"result : {full_name}")

#-------------- indexing ---------------
# name = "vivekanand is a great person"
# print(f"first_name {name[21:]}")
# print(f"first_name {name[:10]}")
# print(f"first_name {name[::-1]}")

# -------------  Tuples  --------------
# use Parentheses
# names = ("mahesh","manish","ayush")
# (bro1 , bro2 ,bro3) = names
# print(f"all brothers name {bro1},{bro2},{bro3}")

# use without Parentheses
# name1 ,name2 = 5,8
# print(f"name1 : {name1}, name2 : {name2}")

#Swap in python using tuples - hame third vairable use nhi krna prta hai
# a , b = 5,10
# print(f"a : {a} , b : {b}")
# a,b = b,a
# print(f"a : {a} , b : {b}")
  
#membership testing using tuples

# students = ("kishor", "rakesh","soniya")
# print(f"Is mahesh in students : {'mahesh' in students}")
# print("soniya" not in students)

#  List -> array in auther language

# l1 = [2,3,1,6,1]
# print(f"list : {l1}")
# sorting
# l1.sort()
# print(l1)
# adding inpartiqular idx
# l1.insert(2 , 10)
# print(l1)
# there are very much functions exist.....

# Operator Overloading
# first_name = "mahesh"
# last_name = "ray"
# full_name = first_name+last_name
# print(f"fullName : {full_name}")

#  set 
# l1 = {2,3,5,6}
# l2 = {3,2,4,2,}

#Union -> part of set(comon values ko nhi lete hai)
# print(f"union : {l1 | l2}")  
#intersection -> part of set(dono main jo comon value ko lete hai )
# print(f"Intersection : {l1 & l2}")

# l3 = set([1,2,3,4,2])
# print(f"unique : {l3}")

# l4 = {1,3,3,2,4,2}  
# print(f"unique : {l4}")

# --------   dictionary -> like a obj in auther language  -----------
# student = {
#     "name":"mahesh ray",
#     "age":20,
#     "roll_No":105,
#     "address":"uttrakhand"
# }

# print(f"dicsnory : {student}")
# print(f"dicsnory all keys : {student.keys()}")
# print(f"dicsnory all items : {student.items()}")
# print(f"dicsnory all values : {student.values()}")


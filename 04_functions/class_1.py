# def sirCook():
#     chai_type = "kali chai"
#     def jrCook():
#         chai_type = "milk_chai"  # yhaa junior function ise access nhi kr pa rha hai
#     jrCook()
#     print("chai change by jr cook",chai_type)
# sirCook()


# using nonlocal keyword

# def sirCook():
#     chai_type = "kali chai"
#     def jrCook():
#         nonlocal chai_type
#         chai_type = "milk_chai"  # yhaa junior function ise access kr pa rha hai
#     jrCook()
#     print("chai change by jr cook",chai_type)
# sirCook()

# # without using global keyword
# chai_type = "hero chai"
# def sirCook():
#     chai_type = "kali chai"
#     def jrCook():
#         nonlocal chai_type
#         chai_type = "milk_chai"  # yhaa junior function parant ka change kr pa rha but golbal ka nhi
#     jrCook()
#     print("chai change by jr cook",chai_type)
# sirCook()

#  using global keyword

# chai_type = "hero chai"
# def sirCook():
#     def jrCook():
#         global chai_type
#         chai_type = "milk_chai"  # yhaa junior function parant ka change kr pa rha but golbal ka nhi
#     jrCook()
#     print("chai change by jr cook",chai_type)
# sirCook()

# Pure function

# def add(a,b):
#     print(a+b)
    
# add(2,4)

# ImPure function -> same input pe output change hota hai

c = 2

def add(x):
    
    global c
    c += x    
    return c

print(add(5))
print(add(5))
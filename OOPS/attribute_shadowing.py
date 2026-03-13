class Chai:
    temp = "hot"
    isMilk = True
    
    
# attribute shadowing

cutting_chai = Chai()

cutting_chai.is_Sweet = True

cutting_chai.temp = "cold"

print("class",Chai.temp)
print("cutting chai",cutting_chai.temp)

#  "del" -> for delete attribute 

del cutting_chai.temp   #delete attribute value from cutting_chai object
print("class",Chai.temp)
print("cutting chai",cutting_chai.temp)   

"""i was delete this attribut but the delete was only object not class 
#thats why is it still send a value of a class value """

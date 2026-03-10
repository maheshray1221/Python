class Company:
    avg_Sailary = 100000  # class Attribute
    role = "full stack developer"  # class Attribute
    
    
# object 1
mahesh = Company()  
mahesh.sirname = "Ray" # instaince attribute

# object 2
tony = Company()
mahesh.sirname = "stark" # instaince attribute
print(mahesh.sirname ,mahesh.avg_Sailary ,mahesh.role)
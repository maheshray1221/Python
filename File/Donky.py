
with open("donky.txt") as f:
    des = f.read()
    
    
if("donky" in des):
    updateDate = des.replace("donky","###")

with open("donky.txt","w") as f:
        f.write(updateDate)
    


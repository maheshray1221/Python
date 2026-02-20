# problem 4 ko reuse krke krna hai with a list


with open("donky.txt") as f:
    des = f.read()
    

harmWord = ["donky","mkc","fuck","fucker"]

for i in harmWord:
    if(i in des):
        print(i)
        updateDate = des.replace(i,"###")
        print(updateDate)

with open("donky.txt","w") as f:
        f.write(updateDate)
    


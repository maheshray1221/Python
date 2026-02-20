

with open("para6.txt") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if("python" in line):
        print("python is exist in the txt file in line no. ",lineno)
        break;
    lineno+=1
else:
    print("python is not found in txt file")
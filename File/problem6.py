
with open("para6.txt") as f:
    para = f.read()
    
if("python" in para):
    print("python is exist in the txt file")
else:
    print("python is not found in txt file")
def allNames():
    yield "tony stark"
    yield "sony deoal"
    yield "monkey the loffy"
    yield "power ranger"
    
names = allNames()

for name in names:
    print("hey",name)
    
    
# another example of generator

def cars():
    yield "bmw"
    yield "supra"
    yield "mini cup"
    yield "aulto"
    
allcar = cars()

# print(allcar) #<generator object cars at 0x000001E24EEA5C70>

print(next(allcar))  # first car -> bmw
print(next(allcar))  # second car -> supra
print(next(allcar))  # third car -> mini cupper
print(next(allcar))  # fourth car -> aulto
print(next(allcar))  # list se bahar jane par give iteration error 
def infinteName():
    count = 1
    while True:
        yield f"hero #{count}"
        count+=1
        
dekhoName = infinteName()
anotherName = infinteName()
for _ in range(5):
    print(next(dekhoName))
    
for _ in range(3):
    print(next(anotherName))
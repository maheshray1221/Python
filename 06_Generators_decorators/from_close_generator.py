def func1():
    yield "tere naam"
    yield "maa tujhe salam"
    
def func2():
    yield "jaduu"
    yield "tarzan"
    
def movies():
    yield from func1()
    yield from func2()

mylist = movies()

mylist.close() # clean up

for movie in movies():
    print(movie)
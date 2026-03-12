from functools import wraps

def decorator(func):
    @wraps(func)
    def mywraper(*args,**kwargs):
        print("before 💕")
        result = func(*args,**kwargs)
        print("after 😺")
        return result
    return mywraper

@decorator
def printName(name):
    print(f"this is a high scorer name {name}")


printName("Mahesh Ray")
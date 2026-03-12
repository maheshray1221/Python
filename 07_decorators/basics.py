from functools import wraps
def mydecoreter(func):
    @wraps(func)
    def wrapper():
        print("before i print ")
        func()
        print("after i print")
    return wrapper


@mydecoreter  # agar main isko nhi likhu too mydecorator function call nhi hoga
def greet():
    print("hello how are you!😂")
    
    
greet()
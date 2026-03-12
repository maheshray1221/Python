from functools import wraps

def adminAuth(func):
    @wraps(func)
    def checkrole(role):
        if role != "admin":
            print("Access denied❌")
            return None # for safty
        else:
            return func(role)
        
    return checkrole


@adminAuth

def myRole(role):
    print("helo i am a admin")
    
myRole("user")
myRole("admin")
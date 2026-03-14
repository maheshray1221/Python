class notfoundError(Exception):
    pass


def fav_chai(chai):
    if chai == "":
        raise notfoundError("chai is missing")
    print("your chai is ready")
    
fav_chai("masala")
fav_chai("")
def myChai(flavor):
    chai = ["masala","cutting","Irani"]
    
    if flavor not in chai:
        raise ValueError ("Unsupported Chai")
    print("your chai is ready")
    
    
myChai("kali")
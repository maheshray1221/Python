def order_Chai(flavor, count):
    try:
        price = {"masala":20}[flavor]
        cost = price*count
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not found in stall")
    except TypeError:
        print("Count must be a Number")
    
order_Chai("cuttin",20)
order_Chai("masala","teo")
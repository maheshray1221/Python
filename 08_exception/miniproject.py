class InvaildChaiType(Exception):pass

def generate_bill(flavor,cup):
    chai_list = {"masala":20,"irani":30}
    try:
        if flavor not in chai_list:
            raise InvaildChaiType("this Chai type not exist in the list")
        """  check cup are number or not """
        if not isinstance(cup,int):
            raise TypeError("cups are always a number")
        cost = chai_list[flavor]*cup
        print(f"Your total bill for {cup} cups of {flavor} chai price is {cost} ")
    except Exception as e:
        print("error",e)
    finally:
        print("Thank you for visiting the stall")
            
generate_bill("masala",3)
generate_bill("mint","three")

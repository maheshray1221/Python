# book_Price = {
#     "jungleBook":200,
#     "english":300,
# }


# try:
#     print(book_Price["hindi"])
# except KeyError:
#     print("your key are not exist in the dictionory")


# print("created by Mahesh")


def serve_chai(flavor):
    try:
        print(f"a {flavor} chai is prepair")
        if(flavor == "unkonwn"):
            raise ValueError("the chai flavor are empty!")
    except ValueError as e:
        print("Error",e)
    else:
        print(f"your {flavor} chai order has delivered")
    finally:
        print("Next coustomer come and order")
        

serve_chai("cutting")
serve_chai("unkonwn")
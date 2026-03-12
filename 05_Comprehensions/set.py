# [expresions loop condition]

# example

# favorite = {
#     "apple",
#     "mango",
#     "orange",
#     "banana",
#     "chiku"
# }


# froute = {my_froute for my_froute in favorite if len(my_froute)>4}

# print(froute)


recipes = {
    "masala chai":["ginger","cardamom","clove"],
    "elaichi chai":["cardamom","milk"],
    "spicy chai":["ginger","black paper","clove"],
}

unique_spices = {spice for ingrediant in recipes.values() for spice in ingrediant}

print(unique_spices)
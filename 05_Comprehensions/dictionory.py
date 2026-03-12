products = {
    "book":150,
    "notebook":40,
    "pen":20,
    "gemetory":60
}

# convert in doller
convertINusd = {product:price/80 for product,price in products.items() }
print(convertINusd)
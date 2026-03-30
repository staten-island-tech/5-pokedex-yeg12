sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def receipt(orders):
    the_recipt = {}
    for i in orders:
        if i ["name"] in the_recipt:
            continue
        else:
            the_recipt[i["name"]] = {
                "price": i["price"],
                "qty": 1
            }
    print(the_recipt)
receipt(sushi_orders)

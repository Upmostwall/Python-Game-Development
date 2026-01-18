shopping_cart = {
    "Items": {
        "Apple": {"Quantity": 4, "Price per unit": 0.5},
        "Banana": {"Quantity": 6, "Price per unit": 0.4},
        "Orange": {"Quantity": 3, "Price per unit": 0.8},
    },
}
 
for item, details in shopping_cart["Items"].items():
    quantity = details["Quantity"]
    price = details["Price per unit"]
    total = quantity * price
    print("{}: Quantity = {}, Price per unit = £{}, Total = £{}".format(item, quantity, price, total))
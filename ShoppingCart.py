#Creating And Printing The Cart
cart = ("Person", ["Chocolate", "Crisps", "CocaCola"])
print(cart)

#Adding Items
cart[1].append("Fries")
print("After Adding Fries:")
print(cart)

#Removing Items
cart[1].remove("Crisps")
print("After Removing Crisps:")
print(cart)

#Replacing Items
cart[1][0] = "Cookies"
print("After Replacing Chocolate:")
print(cart)

#Print Cart User
print("User", cart[0])
print("Items", cart[1])
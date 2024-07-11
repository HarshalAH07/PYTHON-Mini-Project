menu = {
    'Pizza' : 50,
    'Coffee' : 40,
    'Burger' : 100,
    'Fries' : 60,
    'Pasta' : 110
}

print("Welcome to Sparrow's Cafe")
print("Please select your order from the menu below")
for key in menu:
    print(key, ":", menu[key])

order_total = 0

item_1 = input("Enter Your Order = ")

if item_1 in menu :
    order_total += menu[item_1]
    # Adding price of the ordered element in total order
    print(f"Your order for {item_1} has been placed successfully")
else :
    print(f"Your item {item_1} is not available yet!")

another_order = input("Do you want to order something else(YES/NO)")

if another_order == "YES".lower() :
    item_2 = input("Enter Your Order = ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"Your order for {item_2} has been placed successfully")
    else :
        print(f"Your item {item_2} is not available yet!")

print("Thank you for your order! Your total bill is", order_total)
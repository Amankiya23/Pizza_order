from discount import dice_game


size = ["s", "m", "l", "xl"]
price = [40, 50, 60, 75]
sum = 0
extra = 0
price_delivery = 0
total = 0
discount = 0


def pizza_order():
    global sum
    global extra
    global total
    age = int(input("Enter age:"))
    while age >= 18:
        pizza_size = input("Choose the size? s, m, l or xl: ")
        add_extra = input("Do you want extra? y or n: ")
        city = input("select your delivery city beer-sheba (b)/negev(n): ")
        dice_game(total)
        sum += price[size.index(pizza_size)]
        if add_extra == "y":
            extra = extra + 2
            sum += extra
        if city == "b":
            total = sum + 20
        elif city == "n":
            total = sum + 60
        print("the price is:", total, "$")
        next1 = input("Do you want to order another pizza y/n: ")
        if next1 == "n":
            break
    else:
        print("your age is under 18")


pizza_order()

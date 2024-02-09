water = 300
milk = 200
coffee = 100
money = 0
total = 0


def total_money():
    global total
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return total


while True:
    offer = input("What would you like? (Espresso, Latte, Cappuccino): ").lower()
    if offer == "report":
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")
    elif offer == "espresso" or offer == "latte" or offer == "cappuccino":
        if offer == "latte":
            if water < 200:
                print("Not enough water")
                break
            elif milk < 150:
                print("Not enough milk")
                break
            elif coffee < 24:
                print("Not enough coffee")
                break
            else:
                print("Please insert coins.")
                total_money()
                if total < 2.5:
                    print("Sorry that's not enough money. Money refunded.")
                    break
                else:
                    print(f"Here is ${total - 2.5}")
                    print("Here is your latte :) enjoy.")
                    water -= 200
                    milk -= 150
                    coffee -= 24
                    money += 2.5
        if offer == "espresso":
            if water < 50:
                print("Not enough water")
                break
            elif coffee < 18:
                print("Not enough coffee")
                break
            else:
                print("Please insert coins.")
                total_money()
                if total < 1.5:
                    print("Sorry that's not enough money. Money refunded.")
                    break
                else:
                    print(f"Here is ${total - 1.5}")
                    print("Here is your espresso :) enjoy.")
                    water -= 50
                    coffee -= 18
                    money += 1.5
        if offer == "cappuccino":
            if water < 250:
                print("Not enough water")
                break
            elif milk < 100:
                print("Not enough milk")
                break
            elif coffee < 24:
                print("Not enough coffee")
                break
            else:
                print("Please insert coins.")
                total_money()
                if total < 3:
                    print("Sorry that's not enough money. Money refunded.")
                    break
                else:
                    print(f"Here is ${total - 3}")
                    print("Here is your latte :) enjoy.")
                    water -= 250
                    milk -= 100
                    coffee -= 24
                    money += 3
    again = input("Would you like another coffee(y,n): ")
    if again == 'y':
        continue
    else:
        break


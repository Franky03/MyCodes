from resources import MENU, resources
profit=0

def report():
    print('__'*7)
    for k,v in resources.items():
        if k=='Water' or k=='Milk':
            print(f"{k}: {v}ml")
        else:
            print(f"{k}: {v}g")
    print(f"Money: ${profit}")
    print('__'*7)

def sufficient(order):
    for item in order:
        if order[item]> resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def total():
    print("Please insert coins.")
    total = int(input("How many quartes?: "))*0.25
    total += int(input("How many dimes?: "))*0.10
    total += int(input("How many nickels?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def sucessful(money, drink):
    if money>=drink:
        change= round(money- drink, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit+= drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def sub(choice ,option):
    if choice=='cappuccino' or choice=='latte':
        for items in resources:
            resources[items] -= option[items]
    elif choice=='espresso':
        resources['Water']-= option['Water']
        resources['Coffee']-= option['Coffee']

def header():
    print("__"*10)
    print(f"{'Espresso':<10}{MENU['espresso']['cost']:>10}\n{'Latte':<10}{MENU['latte']['cost']:>10}\n{'Cappuccino':<10}{MENU['cappuccino']['cost']:>10}")
    print("__"*10)

is_on=True

header()
while is_on:
    choice= str(input("What would you like? (espresso/latte/cappuccino): ")).strip().lower()
    if choice=='off':
        print("Power Off")
        is_on= False
    elif choice=='report':
        report()
    else:
        drink= MENU[choice]
        if sufficient(drink['ingredients']):
            if sucessful(total(), drink['cost']):
                print(f"Here is your {choice} ☕! Enjoy!")
                sub(choice ,drink['ingredients'])
        
MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5
    },
    "latte": {
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100
        },
        "cost":3.0
    }
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100,
}


def check_report():
    """check available resources and profit"""
    for each_resource in resources:
        print(f"{each_resource}: {resources[each_resource]}")
    print(f"Profit: ${profit}")


def check_resources(order_ingredients):
    """check if the available resources is enough for the drink ingredients"""
    for each_ingredient in order_ingredients:
        if order_ingredients[each_ingredient] > resources[each_ingredient]:
            print(f"Sorry insufficient {each_ingredient}")
            return False
    return True


def process_coin():
    """process the coins inserted and returns the total amount"""
    print("Please insert coins")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickels = int(input("how many nickels?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    return quarters + dimes + nickels + pennies


def transaction_status(money_received, drink_cost):
    """check if the payment is successful return true or fails return false"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry insufficient balance: ${money_received}")
        return False


def make_coffee(drink_name, order_ingredients):
    """deduct the used ingredients from the available resources"""
    for each_ingredient in order_ingredients:
        resources[each_ingredient] -= order_ingredients[each_ingredient]
    print(f"Here is your {drink_name}")

drink_more = True
profit = 0

while drink_more:
    choice = input("What would you like? Espresso/Latte/Cappuccino: ").lower()
    if choice == "no":
        drink_more = False
    elif choice == "report":
        check_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink_info = MENU[choice]
        print(drink_info)
        if check_resources(drink_info["ingredients"]):
            payment = process_coin()
            if transaction_status(payment, drink_info["cost"]):
                make_coffee(choice, drink_info["ingredients"])
    else:
        print(f"Item not found: ({choice})")


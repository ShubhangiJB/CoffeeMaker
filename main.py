from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

close_machine = False

while not close_machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        close_machine = True 
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        if menu.find_drink(choice) != "None":
            drink = menu.find_drink(choice)
            drink_cost = drink.cost
            if coffee.is_resource_sufficient(drink):
                if money.make_payment(drink_cost):
                    coffee.make_coffee(drink)


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

print()

while True:
    ordered_item = input(f"Please select order {order.get_items()}: ").lower()
    if ordered_item == "report":
        money.report()
        machine.report()
    elif ordered_item == "stop":
        break
    else:
        ordered_item = order.find_drink(ordered_item)
        if machine.is_resource_sufficient(ordered_item):
            if money.make_payment(ordered_item.cost):
                machine.make_coffee(ordered_item)

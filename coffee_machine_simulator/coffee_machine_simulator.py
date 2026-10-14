class CoffeeMachine:
    def __init__(self):
        # 1. Initialize the machine's resources and money
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.money = 0.0
        
        # 2. Define the menu with ingredient requirements and costs
        self.menu = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
        }

    def report(self):
        """Prints the current status of all resources and earnings."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money:.2f}")

    def is_resource_sufficient(self, order_ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, required_amount in order_ingredients.items():
            if item == "cost":
                continue
            if self.resources[item] < required_amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Prompts the user to insert coins and calculates the total inserted amount."""
        print("Please insert coins.")
        try:
            quarters = int(input("How many quarters ($0.25)?: ") or 0)
            dimes = int(input("How many dimes ($0.10)?: ") or 0)
            nickels = int(input("How many nickels ($0.05)?: ") or 0)
            pennies = int(input("How many pennies ($0.01)?: ") or 0)
        except ValueError:
            print("Invalid input. Coins must be numbers.")
            return 0.0

        total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        return round(total, 2)

    def is_transaction_successful(self, money_received, drink_cost):
        """Returns True if payment is accepted, or False if money is insufficient."""
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            self.money += drink_cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_coffee(self, drink_name, order_ingredients):
        """Deducts the required ingredients from the resources."""
        for item, required_amount in order_ingredients.items():
            if item != "cost":
                self.resources[item] -= required_amount
        print(f"Here is your {drink_name} ☕. Enjoy!")

    def run(self):
        """Main execution loop for the coffee machine simulator."""
        is_on = True
        print("=== Welcome to the Coffee Machine Simulator ===")
        
        while is_on:
            choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").strip().lower()

            if choice == "off":
                is_on = False
                print("Turning off the coffee machine. Goodbye!")
            elif choice == "report":
                self.report()
            elif choice in self.menu:
                drink = self.menu[choice]
                if self.is_resource_sufficient(drink):
                    payment = self.process_coins()
                    if payment > 0 and self.is_transaction_successful(payment, drink["cost"]):
                        self.make_coffee(choice, drink)
            else:
                print("Invalid option. Please choose from espresso, latte, cappuccino, report, or off.")


if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()

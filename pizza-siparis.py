# -*- coding: UTF-8 -*-
import csv
import datetime


class Pizza:
    def __init__(self, description, price):
        self.description = description
        self.price = price

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class ClassicPizza(Pizza):
    def __init__(self):
        description = "Classic Pizza"
        price = 10.99
        super().__init__(description, price)


class MargheritaPizza(Pizza):
    def __init__(self):
        description = "Margherita Pizza"
        price = 12.99
        super().__init__(description, price)


class TurkPizza(Pizza):
    def __init__(self):
        description = "Turk Pizza"
        price = 14.99
        super().__init__(description, price)


class DominosPizza(Pizza):
    def __init__(self):
        description = "Dominos Pizza"
        price = 16.99
        super().__init__(description, price)
classic_pizza = ClassicPizza()
class Sauce(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()


class Olives(Sauce):
    def __init__(self, pizza):
        description = "Olives"
        price = 1.99
        super().__init__(pizza)
        self.description = self.pizza.get_description() + f", {description}"
        self.price = self.pizza.get_cost() + price

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class Mushrooms(Sauce):
    def __init__(self, pizza):
        description = "Mushrooms"
        price = 1.99
        super().__init__(pizza)
        self.description = self.pizza.get_description() + f", {description}"
        self.price = self.pizza.get_cost() + price

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class GoatCheese(Sauce):
    def __init__(self, pizza):
        description = "Goat Cheese"
        price = 2.99
        super().__init__(pizza)
        self.description = self.pizza.get_description() + f", {description}"
        self.price = self.pizza.get_cost() + price

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class Meat(Sauce):
    def __init__(self, pizza):
        description = "Meat"
        price = 3.99
        super().__init__(pizza)
        self.description = self.pizza.get_description() + f", {description}"
        self.price = self.pizza.get_cost() + price

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price
class Onions(Sauce):
    def __init__(self, pizza):
        description = "Onions"
        price = 1.99
        super().__init__(pizza)
        self.description = self.pizza.get_description() + f", {description}"
        self.price = self.pizza.get_cost() + price

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class Corn(Sauce):
    def __init__(self, pizza):
        description = "Corn"
        price = 1.99
        super().__init__(pizza)
        self.description = self.pizza.get_description() + f", {description}"
        self.price = self.pizza.get_cost() + price

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price
def read_menu():
    with open("menu.txt", "r", encoding='utf-8') as f:
        return f.read()

def get_user_input(pizza_types, sauce_types):
    print("Welcome to our pizza order system!")
    print("Please choose a pizza from the menu:")
    print(pizza_types)
    pizza_choice = input().strip()

    print("\nPlease choose a sauce for your pizza:")
    print(sauce_types)
    sauce_choice = input().strip()

    return pizza_choice, sauce_choice

def get_total_price(pizza_choice, sauce_choice):
    # get the pizza and sauce objects based on user input
    # calculate the total price and return it
    pass

def get_user_info():
    print("\nPlease enter your name:")
    name = input().strip()

    print("\nPlease enter your ID number:")
    id_number = input().strip()

    print("\nPlease enter your credit card number:")
    credit_card_number = input().strip()

    print("\nPlease enter your credit card password:")
    credit_card_password = input().strip()

    return name, id_number, credit_card_number, credit_card_password

def save_order_to_database(name, id_number, credit_card_number, description, total_price, credit_card_password):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("Orders_Database.csv", mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, id_number, credit_card_number, description, total_price, timestamp, credit_card_password])
def main():
    pizza_types = "Classic, Margherita, Turk Pizza, Dominos Pizza"
    sauce_types = "Olives, Mushrooms, Goat Cheese, Meat, Onions, Corn"
    menu = read_menu()

    print(menu)
    pizza_choice, sauce_choice = get_user_input(pizza_types, sauce_types)
    total_price = get_total_price(pizza_choice, sauce_choice)
    name, id_number, credit_card_number, credit_card_password = get_user_info()
    description = f"{pizza_choice} pizza with {sauce_choice} sauce"
    save_order_to_database(name, id_number, credit_card_number, description, total_price, credit_card_password)

if __name__ == "__main__":
    main()
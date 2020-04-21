# Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

class Pizza:

    def __init__(self):
        self.size = 0
        self.crust = ""
        self.toppings = list()

# Add a method for interacting with a pizza's toppings, called add_topping.


    def add_topping(self, topping):
        self.toppings.append(topping)


# Add a method for outputting a description of the pizza (sample output below).


    def print_order(self):
        toppings = ", ".join(self.toppings)
        print(f"I would like a {self.size} inch, {self.crust} pizza with {toppings}")

# Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.crust = "deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()

# You should produce output in the terminal similiar to the following string.

# "I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."

meat_lovers = Pizza()
meat_lovers.size = 9000
meat_lovers.crust = "Stuffed"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Jalapenos")
meat_lovers.add_topping("Banana Peppers")
meat_lovers.print_order()
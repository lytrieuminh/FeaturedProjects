# Let's create a class to keep inventory of grocery items at a store. We'll create many items, customizing them using the constructor.

class Grocery_Item:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.has_discount = discount

    def display_info(self):
        print(self.name, "is $", self.price)


apple = Grocery_Item("apple", 1, False)
cheerios = Grocery_Item("cheerios", 4, True)

apple.display_info()
print("does", cheerios.name, "have a discount?", cheerios.has_discount)

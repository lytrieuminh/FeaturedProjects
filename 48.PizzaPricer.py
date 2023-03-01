# A pizzashop wants to know how much the ingredients of each type of pizza costs.
# They have a program to help, but it needs fixing.

menu = ["margherita", "vegetable", "pepperoni"]

margherita = []
vegetable = ["peppers", "mushrooms", "onions"]
pepperoni = ["peppers", "chilli", "salami"]

ingredients = {"peppers": 0.8,
               "mushrooms": 0.5,
               "onions": 0.6,
               "chilli": 0,
               "salami": 1.5
               }

choice = vegetable

base_cost = 2.5
extra_cost = 0

for item in choice:
    extra_cost += ingredients[item]

total_cost = base_cost + extra_cost
print(total_cost)

# Chapter1: Creating the variables
# Let's use our knowledge about data types and formatted strings to create a tip calcultor for your next evening out!
# We'll start by creating a variable for the base meal cost, one for the tip percentage we want to give, and lastly, the tax percentage.

bill = 20
tip_percentage = 0.15
tax_percentage = 0.067


# Chapter2: Making the calculator
# Let's do the math! First, we'll calculate the amount of tax due, then the tip, and finally the total sum we'll have to pay.

tip = bill * tip_percentage
print(f"Tip: {tip}")

tax = bill * tax_percentage
print(f"Tax: {tax}")

total = bill + tip + tax
print(f"Total: {total}")

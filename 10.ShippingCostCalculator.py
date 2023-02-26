# Chapter1: Shipping destination
# Let's use our knowledge of if, elif, and else statements to code a shipping cost calculator.

international_shipping = True

total = 150
shipping_cost = 0

if international_shipping:
    shipping_cost += 15
    print("International base cost applied")


# Chapter2: Extra costs
# We'll update the shipping cost based on the total purchase. The higher the total, the cheaper the shipping will be.

if total <= 50:
    shipping_cost += 20
elif total <= 100:
    shipping_cost += 15
else:
    shipping_cost += 5
print(f"Shipping cost: {shipping_cost}")

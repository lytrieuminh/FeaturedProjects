# Let's use pur knowledge of number equality to write code
# that tracks sales data for an online jeans retailer.

stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print("Hit jeans sale target: ")
print(target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock:")
print(in_stock)

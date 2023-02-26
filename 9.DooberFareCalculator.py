# Chapter1: We'll use our knowledge of if, elif and else conditionals to calculate a rideshare fare
# depending on the chosen ride type.

ride_type = "Black"
credits = 4

ride_price = 0
final_price = 0

if ride_type == "DooberX":
    ride_price = 20.5
elif ride_type == "Black":
    ride_price = 37.9
else:
    ride_price = 18.7

print("Ride price:")
print(ride_price)


# Chapter2: Now that we've calculated the price depending on the ride type.
# Now use in-app credits.

if credits > 0:
    final_price = ride_price - credits

print("Final price:")
print(final_price)

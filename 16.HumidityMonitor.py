# Let's use a list to manage soil humidity data received deom a greenhouse monitor. We'll use the list to track at over five days.

humidity_level = [87, 83, 89, 88, 87]

humidity_level.insert(0, 90)
print(humidity_level)

humidity_level.pop()
print(humidity_level)

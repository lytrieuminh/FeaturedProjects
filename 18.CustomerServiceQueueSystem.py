# Let's use our lists skills to sort a list of customers and assign them to the first available customer service desks
# We'll sort the list of customers alphabetically to decide who goes first.

customers = ["Filip", "Miranda", "Ariah", "Laurence", "Shahid"]

free_counters = [11, 20, 14, 6, 4]

customers.sort()
free_counters.sort()

customer = customers[0]
counter = free_counters[0]

print(customer)
print("Visit counter:")
print(counter)

# Largest
# Let's use our knowledge of lists to analyze an unsorted dataset of the ten largest lakes in the United States.

sizes = [7340, 2117, 22300, 31700, 1679, 1014, 23000, 9910, 685]

largest = max(sizes)

print("Largest lake in sq mi:")
print(largest)


# Smallest
# It's time to find the smallest lake in the dataset.

smallest = min(sizes)

print("10th largest lake in sq mi:")
print(smallest)

difference = largest - smallest

print("Difference between lakes in sq mi:")
print(difference)

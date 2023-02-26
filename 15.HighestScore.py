# Let's create some code that helps an arcade machine find the highest score from a list of scores without the help max()
# We'll use a list, for-loop, and companrison to go through the scores and check if one score is higher than the last
# We'll store the first value of the list in a variable then loop through the list and update the variable if we find a bigger value.

user_scores = [12, 42, 55, 100, 11, 22]
highest = user_scores[0]

for score in user_scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")

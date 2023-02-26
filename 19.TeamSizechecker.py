# Chapter1: Checking team sizes
# Let's use conditionals and list length to check team sizes and decide on the number of rounds left in an game.

team_1 = ["Mia", "Lisa", "Liam"]
team_2 = ["James", "Ty", "Ava"]

size_1 = len(team_1)
size_2 = len(team_2)


# Chapter2: Caculating the rounds left
# Now that we know that the teams have the same size, we can divide how many rounds they can play based on their size.

if size_1 != size_2:
    print("Teams must have the same size!")
else:
    print("Game on!")

if size_1 == 3:
    print("Rounds left: 3")
elif size_1 == 2:
    print("Rounds left: 2")
else:
    print("Final round!")

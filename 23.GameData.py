# Round1: Let's use our f-string knowledge to keep track of two players and the data they generate during a round-based game.
# We'll start by displaying the players, followed by the current round number, and finally the winner.

player_1 = "Sam"
player_2 = "Alex"
current_round = 1

print("Game on!")
print(f"player 1: {player_1}")
print(f"player 2: {player_2}")
print("--------------------------")

print(f"Round {current_round}!")
player_1_score = 10
player_2_score = 13
print(f"{player_2} wins with {player_2_score} to {player_1_score}")
print("--------------------------")


# Round2: On to the second round! We'll update the player's scores, calculate the difference, and display the winner.

print(f"Round {current_round + 1}!")
player_1_score = 20
player_2_score = 5
print(f"{player_1} defeats {player_2} by {player_1_score - player_2_score} points")

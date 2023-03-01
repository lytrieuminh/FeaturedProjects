# Let's make an automated quiz marker, which checks answers are correct before a user can move on.

answers = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

responses = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

if responses[-1] == answers[len(responses)-1]:
    correct = True
else:
    correct = False

if not correct:
    del responses[-1]
    print("Sorry, please try the last question again!")

elif len(responses) < len(answers):
    print('Quiz not complete.')
    correct = str(len(responses))
    print("You've got " + correct +
          " answers correct so far, please add an answer for the next question.")

else:
    print("Well done, you have completed the quiz!")

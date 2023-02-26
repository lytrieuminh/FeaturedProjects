# Chapter1: Creating variables
# Let's use our knowledge of while loops to see how the amount stored in a bank account increases over time, with a given interest rate.

account = 100
interest_rate = 0.004
years = 3

print(f"Initial amount: {account}")


# Chapter2: Making calculations

counter = 1
while counter <= years:
    accrued_interest = account * interest_rate
    account += accrued_interest
    print(f"year {counter}: {account}")
    counter += 1

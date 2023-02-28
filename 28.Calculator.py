# Let's create a simple calculator that can add, substract, and multiply numbers.
# We'll create a function that takes two numbers and an operator as its parameters.

def calculator(num_1, num_2, op):
    result = 0

    if op == "+":
        result = num_1 + num_2
    elif op == "-":
        result = num_1 - num_2
    elif op == "*":
        result = num_1 * num_2
    print(f"{num_1} {op} {num_2} = {result}")


calculator(5, 10, "*")

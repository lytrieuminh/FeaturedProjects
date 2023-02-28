# Let's use our knowledge of using lists with functions to find out
# if a user is a common friend amongst two other users.

def is_common_friend(user, friends_a, friends_b):
    is_friend_a = friends_a.count(user) >= 1
    is_friend_b = friends_b.count(user) >= 1

    # If user is a common friend, then it should be in both lists, so both "is_friend_a" and "is_friend_b" should be True.
    # The easy way to check if two booleans are True is the "&" operator, which gives True, when both sides are True
    # Create the variable "is_common" to save the resulting boolean.
    is_common = is_friend_a & is_friend_b

    return is_common


friends_joe = ["Sam", "Alex", "Zoe"]
friends_may = ["Kim", "Alex", "Cy", "Ted"]

common_alex = is_common_friend("Alex", friends_joe, friends_may)
print(f"Alex is a common friend: {common_alex}")

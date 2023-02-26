# Chapter1: Set up
# Let's use for loops to speed up the process of creating multiple discount coupon codes.

base = "www.homeflix.com"
coupon = "signup/coupon"
discount = 50
amount = 4


# Chapter2: Coupon
# F-strings will help us quickly create the URLs we need for the coupon codes.

for num in range(amount):
    print(f"{base}/{coupon}/{discount}/{num}")

print(f"{amount} coupons created")

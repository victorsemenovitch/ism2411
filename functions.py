# Self-Assessment
# Q1: The first bug was a missing colon. I learned to check my code carefully.
# Q2: apply_discount takes a price and tier and returns the discounted price.
# Q3: I used AI to help understand and complete the exercises.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")

# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---
# Bug 1: The total needs to add each sale.
# Bug 2: The for loop needs a colon.
# Bug 3: The while loop goes one index too far.

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---
x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# Scope means a variable inside a function can be
# different from a variable outside the function.
# The global x stays 100.
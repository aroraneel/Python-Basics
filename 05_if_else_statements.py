# ============================================
# If-Else Statements
# ============================================

# If-else statements are used to make
# decisions based on conditions.

age = int(input("Enter your age: "))
has_ticket = True
price = 10.00

# Check the person's age
if age >= 65:
    print("You are a senior citizen")
    print(f"The ticket price for a senior citizen is ${price * 0.75}")
elif age >= 18:
    print("You are an adult:")
    print(f"The ticket price for an adult is ${price}")
else:
    print("You are a child")
    print(f"The ticket price for a child is ${price * 0.5}")

# Check if the person has a ticket
if has_ticket:
    print("You may enter, you have a ticket")
else:
    print("You may buy a ticket")
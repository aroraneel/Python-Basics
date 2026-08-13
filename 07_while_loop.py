# ============================================
# While Loop
# ============================================

# A while loop is used to repeat a block of code
# as long as a condition remains True.

# --------------------------------------------
# Basic While Loop
# --------------------------------------------

count = 1

while count <= 5:
    print(count)
    count += 1

# --------------------------------------------
# While Loop with User Input
# --------------------------------------------

name = input("Enter Your Name: ")

while name == "":
    print("Name cannot be empty.")
    name = input("Enter Your Name: ")

print(f"Hello {name}!")

# --------------------------------------------
# While Loop for Input Validation
# --------------------------------------------

age = int(input("Enter Your Age: "))

while age < 0:
    print("Age cannot be less than 0.")
    age = int(input("Enter Your Age: "))

print(f"You are {age} years old.")

# --------------------------------------------
# While Loop with Break
# --------------------------------------------

while True:
    number = int(input("Enter a positive number: "))

    if number > 0:
        break

    print("Please enter a positive number.")

print(f"You entered: {number}")
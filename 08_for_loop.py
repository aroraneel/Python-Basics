# ============================================
# For Loop
# ============================================

# A for loop is used to iterate over a sequence
# or repeat a block of code a specific number of times.

# --------------------------------------------
# For Loop with Range
# --------------------------------------------

for i in range(10):
    print(i)

# --------------------------------------------
# For Loop with Start and End
# --------------------------------------------

for i in range(1, 11):
    print(i)

# --------------------------------------------
# For Loop with Step
# --------------------------------------------

for i in range(1, 11, 2):
    print(i)

# --------------------------------------------
# For Loop with String
# --------------------------------------------

name = "Raj Singh"

for letter in name:
    print(letter)

# --------------------------------------------
# For Loop with End Parameter
# --------------------------------------------

for letter in name:
    print(letter, end=" ")

print()

# --------------------------------------------
# For Loop with Different Step
# --------------------------------------------

for i in range(1, 11, 3):
    print(i)

# --------------------------------------------
# Countdown Using For Loop
# --------------------------------------------

for i in range(10, 0, -1):
    print(i)

print("Happy New Year!")

# --------------------------------------------
# Countdown Timer
# --------------------------------------------

import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("Happy New Year!")
# ============================================
# Lists
# ============================================

# A list is used to store multiple values in
# a single variable. Lists are mutable, meaning
# their elements can be changed.

# --------------------------------------------
# Creating a List
# --------------------------------------------

fruits = ["Apple", "Orange", "Banana", "Coconut"]

# Display the entire list
print(fruits)

# --------------------------------------------
# Accessing List Elements
# --------------------------------------------

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# --------------------------------------------
# List Indexing
# --------------------------------------------

# The first element has an index of 0.
# The second element has an index of 1.
# The third element has an index of 2.
# The fourth element has an index of 3.

print(fruits[0])

# --------------------------------------------
# Loop Through a List
# --------------------------------------------

for fruit in fruits:
    print(fruit, end=" ")

print()

# --------------------------------------------
# Changing List Elements
# --------------------------------------------

fruits[0] = "pineapple"
fruits[3] = "Mango"

print(fruits)

# --------------------------------------------
# Adding Elements with append()
# --------------------------------------------

fruits.append("Mango")

print(fruits)

# --------------------------------------------
# Removing Elements with remove()
# --------------------------------------------

fruits.remove("Banana")

print(fruits)

# --------------------------------------------
# Removing Elements with pop()
# --------------------------------------------

fruits.pop(0)

print(fruits)

# --------------------------------------------
# Clearing the List
# --------------------------------------------

fruits.clear()

print(fruits)
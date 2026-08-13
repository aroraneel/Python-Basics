# ============================================
# Sets
# ============================================

# A set is an unordered and mutable collection.
# Sets are created using curly braces.

# --------------------------------------------
# Creating a Set
# --------------------------------------------

fruits = {"Apple", "Orange", "Banana", "Coconut"}

# Display the entire set
print(fruits)

# --------------------------------------------
# Sets Are Unordered
# --------------------------------------------

# The order of elements in a set can change.
# Sets cannot be accessed using an index.

print(fruits)

# --------------------------------------------
# Adding Elements with add()
# --------------------------------------------

fruits.add("Mango")

print(fruits)

# --------------------------------------------
# Removing Elements with remove()
# --------------------------------------------

fruits.remove("Coconut")

print(fruits)

# --------------------------------------------
# Sets Do Not Allow Duplicates
# --------------------------------------------

fruits.add("Apple")
fruits.add("Apple")
fruits.add("Apple")

print(fruits)

# --------------------------------------------
# Membership Testing
# --------------------------------------------

if "Apple" in fruits:
    print("Apple was found.")
else:
    print("Apple was not found.")

# --------------------------------------------
# Membership Testing with User Input
# --------------------------------------------

search_fruit = input("Enter a fruit to search for: ")

if search_fruit in fruits:
    print(f"{search_fruit} was found.")
else:
    print(f"{search_fruit} was not found.")

# --------------------------------------------
# Clearing the Set
# --------------------------------------------

fruits.clear()

print(fruits)
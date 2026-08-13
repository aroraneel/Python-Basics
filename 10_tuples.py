# ============================================
# Tuples
# ============================================

# A tuple is an ordered and immutable collection.
# Tuples are created using parentheses.

# --------------------------------------------
# Creating a Tuple
# --------------------------------------------

fruits = ("Apple", "Orange", "Banana", "Coconut")

# Display the entire tuple
print(fruits)

# --------------------------------------------
# Accessing Tuple Elements
# --------------------------------------------

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# --------------------------------------------
# Tuple Indexing
# --------------------------------------------

# The first element has an index of 0.
# The second element has an index of 1.
# The third element has an index of 2.
# The fourth element has an index of 3.

print(fruits[0])

# --------------------------------------------
# Tuple Immutability
# --------------------------------------------

# Tuple elements cannot be changed after
# the tuple is created.

# fruits[0] = "Pineapple"

# --------------------------------------------
# Tuple Does Not Support append()
# --------------------------------------------

# Tuples cannot have new elements added.

# fruits.append("Mango")

# --------------------------------------------
# Tuple Does Not Support remove()
# --------------------------------------------

# Tuples cannot have elements removed.

# fruits.remove("Apple")
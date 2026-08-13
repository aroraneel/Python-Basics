# ============================================
# Logical Operators
# ============================================

# Logical operators are used to combine
# multiple conditions in Python.

# --------------------------------------------
# OR Operator
# --------------------------------------------
# Returns True if at least one condition is True.

print("----- OR Operator -----")

temp = 37
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is on")

print()

# --------------------------------------------
# AND Operator
# --------------------------------------------
# Returns True only if all conditions are True.

print("----- AND Operator -----")

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY outside")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY outside")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY outside")

print()

# --------------------------------------------
# NOT Operator
# --------------------------------------------
# Reverses the result of a condition.
# True becomes False, and False becomes True.

print("----- NOT Operator -----")

temp = 28
is_sunny = False

if temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY outside")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY outside")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY outside")

print()
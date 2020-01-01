# Data Structures:
# There are 4 main data structures needed to know, but you can find more with libraries
# - List
# - Set
# - Tuple
# - Dictionary

# Let's understand whats so special about these data structures before playing with them

# Key Words:
# Mutable - Can be edited or altered
# Immutable - Can't be edited or altered
# Ordered - Has an order
# Unordered - Doesn't have an order

# A list is an ordered and mutable data structure (denoted by [])
# A set is an unordered and mutable data structure (denoted by {})
# A tuple is an ordered and immutable data structure (denoted by ())
# A dictionary is an ordered and mutable data structure (denoted by {:})

# Just making my job easier. If you know what I'm doing that's great!

def check(a):
    print(f"Value: {a}")
    print(f"Type: {type(a)}")

# Let's see some examples:

a = [1, 2.5, "banana"]  # Using a again
check(a)  # Prints out the value and type

# Let's print a specific value instead of the whole list
print(a[0])  # Prints 1

# But why does that print 1 when we fed the value 0?
# The answer is LIST INDEXING
# Lets think of the list again:
# [     1,           2.5,           "banana"]
#   1st value     2nd value        3rd value
# We can ask for a specific item of the list.

# I want to see the second value in the list
print(a[2])  # Prints "banana"

# Why did it print "banana" when I put in 2?
# Because of ZERO LIST INDEXING
# Lists in python are started from the 0 and goes to the last value
# First Value = 0
# Second Value = 1
# Third Value = 2
# nth Value = n - 1

# I want to see the second value in the list
print(a[1]) # Prints 2.5

# Lets create a big list and choose the last value of it
a = [i for i in range(0,100)] # Making a list with values from 0-99
# Instead of doing print(a[99]) to get the last value we can use negative numbers
print(a[-1])

# I want a list of the values from places 0-10 from a
print(a[:10])

# What just happened? Why are there colons?
# You can use colons as a way to "select" data
# It follows the format list[start:end]
# Notice how I didn't put a start value. This is because when not provided, Python defaults to the start of the list
# If we were to choose values from places 90-100, we would write:
print(a[90:])
# Because Python uses the end value when not provided

# I want a list from 25-50 from our bigger list:
print(a[25:50])

# I don't want the values after 40, so lets drop them
del a[40:]
print(a)

# Sets:
# Refer to the definition of a set above.
# Lets make one

b = {1,2,3,3,4,5}
check(b)

# Why has the value 3 only appeared once?
# Sets automagically remove duplicate items. This can be useful in a variety of ways.
# Be warned however, sets do not have a order and can jumble themselves up.

a = [1,2,3,3,4,4,5,2,3,7]
print(set(a)) # Remove duplicates
print(list(set(a))) # Remove duplicates and make a list

# We can also remove items from here
b.remove(4) # Removes the number 4 from our set
print(b)

# Tuples:
# Tuples are immutable, as in you can not change them!
# They may look like you have changed them, but they haven't really
# Python creates a new tuple based on your specifications and assigns it, while the old tuple is still in memory

c = (1,2,3,3,4)
check(c)

# You can even define a tuple as such:

c = 1,2,3,4
check(c)

# Dictionaries:
# Dictionaries are denoted like sets but store more information.
# They are mutable, ordered, and can't have duplicate keys (you'll see)

d = {
    "France": "Paris",
    "snacks": ["apples", "bananas", "oranges"],
    "price": 10.00
}

# The format of a dictionary is as follows
# {
#     "key": value,
#     "key2": value2,
#     ...
#     "keyn": valuen
# }
# Values can support any data type and data structure. It can even hold other dictionaries!
# A key-value pair is known as an element
# Unlike other data structures, dictionaries don't follow zero list indexing. Rather they use keys to track items

# Let's see what the key "France" has

print(d["France"])

# I want to add a new entry
d["games"] = "uno","monopoly"
print(d) # Notice how "games" is added as a tuple.

# I want to delete an entry
del d["snacks"]
print(d)

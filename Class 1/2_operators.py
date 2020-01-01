# As any computer should, it should be able to compute and perform operations
# Math is very important in logical programming and Python has some default operators

# Let's check out what we already know that can be done:
print("5 + 6 = ",5+6) # Addition

print("6 - 5 = ",6-5) # Subtraction

print("5 * 6 = ",5*6) # Multiplication

print("5 / 6 = ", 5/6) # Division

print("5 ** 2 = ",5**2) # Exponentiation 

# There are some additional operators Python provides:

print("5 % 6 = ", 5%6) # Modulus (The remainder of a division.)

print("5 // 6 = ", 5//6) # Floor Division (The division with no remainder.)

# Math can be done with variables too:
a = 4
b = 12 + a
c = 3*a + (b/4) # Can you guess what c is?
print("c = ", c)

# Comparison operators:
# Python also knows how to deal with items that are bigger or smaller or equal
# The results of comparison operations return a boolean value!

a = 1
b = 2

print(a == b) # '==' means equals to
print(a != b) # '!=' means not equal to
print(a > b) # '>' means greater than
print(a < b) # '<' means less than
b = 1
print(a >= b) # '>=' means greater than or equal to
print(a <= b) # '<=' means less than or equal to

# Notice how everything printed is either true or false

# Assignment operators:
# You have seen some assignment operators already. Let's see them again

a = 4 # '=' assigns one value to another. This is pretty much the main one.

# What if I wanted to add a counter that counts how many times a person types "Hello" in a sentence
# I can get the detection done, but what about the math part?

# We could do it like this:
a = 0
a = a + 1
# But this really annoying and extra work

# Python allows us to have assignment operators that give some shortcuts
# (If you want to see the results, use print statements)
a += 1 # Add 1 to the previous value of a
a -= 1 # Remove 1 to the previous value of a
a *= 2 # Multiply the previous value of a by 2
a /= 1 # Divide the previous value of a by 1
a **= 2 # Exponentiate the previous value of a by 2
a //= 2 # Floor divide the previous value of a by 2
a %= 1 # Moduluo the previous value of a by 1

# String operators:
# There are different things we can do to strings.

# We can combine strings with the addition operator.
a = "hello" + " " + "world"
print(a) # Prints hello world

# We can also repeat strings with the multiplication operator.
a = "hello" * 10
print(a)

# You can also find the length:
a = "hey"
print(len(a)) # Would print 3 

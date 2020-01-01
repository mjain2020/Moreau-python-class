# Loops are structures that let you repeat Python code over and over

# Key Words
# Iterate = To do over and over again, to repeat
# Nested loop = A loop inside another loop

# First, we'll talk about FOR LOOPS.
# We can use loops to perform an action one time for every object in a list
# Let's look at an example.

dog_breeds = ["bulldog", "poodle", "pug"]

# Print each breed:
for breed in dog_breeds:
  print(breed)

# This is the structure:
# for (temporary value) in (a list)
#   do something

# Indentation is important!
# Remember to indent everything inside your loops.

# We can also use loops to perform an action a specific number of times in a row.
# Print the numbers 0, 1, 2:
for i in range(3):
  print(i)

# Print "WARNING" 3 times:
for i in range(3):
  print("WARNING")
  
# In a loop, the break keyword escapes the loop, regardless of the iteration number
# Once break executes, the program will perform everything after the loop.
# Let's see an example.

numbers = [0, 254, 2, -1, 3]

for num in numbers:
  if (num < 0):
    print("Negative number detected!")
    break
  print(num)

print("Done")

# In this example, the output would be:
# 0
# 254
# 2
# Negative number detected!
# Done

# We also have the continue keyword
# It's used inside a loop to skip the remaining code inside the loop code block, and begin the next loop iteration
# Let's see an example.

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)

# In this example, the output would be:
# 1
# 2
# 4
# 5
# 2

# Now, let's talk about WHILE LOOPS.
# A while loop will repeatedly execute a code block as long as a condition evaluates to True

# The condition of a while loop is always checked first before the block of code runs
# So if the condition is not met initially, then the code block will never run

# This loop will only run 1 time
hungry = True
while hungry:
  print("Time to eat!")
  hungry = False

# This loop will run 5 times
i = 1
while i < 6:
  print(i)
  i += 1

# We can also have nested loops, which are loops inside other loops

# Example
dog_breeds = ["bulldog", "poodle", "pug"]

# Print each breed:
for breed in dog_breeds:
  for i in range(2):
    print(breed)

# This would give the output
# Bulldog
# Bulldog
# Poodle
# Poodle
# Pug
# Pug 


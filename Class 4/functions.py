# Functions!
# Sometimes, some tasks need to be performed multiple times within a program
# Let's look at an example.

def check_leap_year(year): 
  if year % 4 == 0:
    return "It is a leap year."
  else:
    return "It is not a leap year."

# A function may be defined using the def keyword. 
# Function definitions may include parameters, which provide data input to the function.
# Functions may also return a value using the return keyword followed by the value to return.

# In this example, a function check_leap_year is defined with parameter x.
# The function takes the year, finds the remainder when it's divided by 4, and returns a string based on the result.

# This is the general structure for a function:
# def function_name(first_parameter, second_parameter, and so forth):
#    { BODY }
#    return something

# Let's go step by step.
# For the first line, we don't have to have parameters.
# But you always need def, followed by the function name, parentheses, and a colon.

def do_my_homework():
	pass

# Python uses indentation to identify blocks of code
# Code within the same block should be indented at the same level
# All code under a function declaration should be indented to identify it as part of the function
# There can be additional indentation within a function to handle other statements such as for and if,
# so long as the lines are not indented less than the first line of the function code.

# Sometimes functions require input to provide data for their code
# This input is defined using parameters.

# Parameters are variables that are defined in the function definition
# They are assigned the values which were passed as arguments when the function was called, elsewhere in the code.

def write_a_book(character, setting, special_skill):
	print(character + " is in " + 
        setting + " practicing her " + 
        special_skill)

# For example, the function definition defines parameters for a character, a setting, and a skill
# They are all used as inputs to write the first sentence of a book

# Let's look at another example.
def ready_for_school(backpack, pencil_case):
  if (backpack == 'full' and pencil_case == 'full'):
    print ("I’m ready for school!")

# Python functions can also have multiple parameters
# Just as you wouldn’t go to school without both a backpack and a pencil case, 
# functions may also need more than one input to carry out their operations.

# To define a function with multiple parameters, parameter names are placed in a comma-separated list,
# within the parentheses of the function definition.

# Let's see another example.
def findvolume(length=1, width=1, depth=1):
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    return length * width * depth

# Python functions can be defined with named arguments which may have default values provided.

# Let's go back to our first example function.
def check_leap_year(year): 
  if year % 4 == 0:
    return str(year) + " is a leap year."
  else:
    return str(year) + " is not a leap year."
    
 # A return keyword is used to return a value from a Python function
 # The value returned from a function can be assigned to a variable which can then be used in the program
 # In this example, the function check_leap_year returns a string which indicates
 # if the passed parameter is a leap year or not.
 
 # Now, what if you want to return multiple values?
def square(x, y, z):
  x_squared = x * x
  y_squared = y * y
  z_squared = z * z
 
 # Return all three values: return x_squared, y_squared, z_squared
 # All values that should be returned are listed after the return keyword and are separated by commas.







 # Let's learn two new terms: global and local variables!

 # The variables you declare inside a function are local variables...
 # This means that those variables can only be used within the function, not outside

 # How about global variables?

 x = 4

 def square(x, y, z):
 	x_squared = x * x
 	y_squared = y * y
 	z_squared = z * z

 # x is a global variable since it's inside the program but outside of the function
 # x can be used anywhere in the program whether it be inside or outside any function

#What's the point of defining functions when you can't use them?

#Here's how we call a function in python...

check_leap_year(1985)

#All you have to do is write the name of the function and then follow it with parentheses
#These parentheses contain the value you are assigning the arguments (or parameters)
#In this example, you are assigning the year parameter the value 1985

#how about if you have no parameters?

do_my_homework() #Then you don't have to put in any values for your parameters (since you don't have any!)

#it's important to remember that the number of values you pass in must be equal to the number of parameters you have...

#For example:

write_a_book("Mellie", "The Forest", "invisibility")

#Since write_a_book has 3 parameters, you MUST give in 3 values
#else, you will get a syntax error :(

#Also remember that the value you pass in must match the paramater type

#For example:

def make_a_sandwich(number_of_slices, name):
	calories = number_of_slices * 60
	return name	

#Here, number_of_slices is an integer while name is a string
#So when calling the function...

make_a_sandwich(4, "The Monster Sandwich")

#The first parameter must be an integer because number_of_slices is an integer
#The second parameter must be a string because name is a string

#Note: ORDER MATTERS...

make_a_sandwich("The Monster Sandwich", 4)

#You will get an error because number_of_slices is given a string even though it is used as an integer

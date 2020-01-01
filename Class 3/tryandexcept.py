#Let's learn about try and except!
#Basically if you have an error in your code, you can use try and except blocks to catch the error
#For example...

try:
  print(x)
except:
  print("X is not defined :(")

#What's happening here? Well, you are "try"ing out your code <print(x)>.
#Since we never defined x and are still trying to print it, the program raises an error!
#Therefore, the except statement is called and its contents are printed!

#What happens if your code is perfectly fine?

try:
  print("Hello World")
except:
  print("syntax error...")
  
#Since there is nothing wrong with the contents of <print("Hello World")>, the try statement is executed and the except statement is skipped!

#You can also have multiple except statements!

try:
  print(x)
except NameError:
  print("x is not defined!")
except:
  print("There is some other error")
  
#When you have multiple except statements, you have 2 options:
#       1. Leave one except statement as "except:" specify what error every other except statement is trying to catch.
#       2. Specify what error each except statement is trying to catch. 

#Here, since you have a NameError, your program executes the first except statement
#Note that having just "except:" means that it will catch any other error types that you don't mention explicitly
#Let's see an example of that:

x = "Hello World!"
try:
  print(x + True)
except NameError:
  print("X is not defined :(")
except:
  print("Some other error occured --")
  

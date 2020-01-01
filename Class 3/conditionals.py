# Let's learn about if statements!
# Think of if statements as boolean conditions that can be true or false
# if (true), then execute "body"
# if (false), then don't execute "body"
# The body is group of statements that are run when boolean condition is true
# Example:
x = 4
y = 5
if ( x < y ) :
  print("x is less than y")
# here, (x < y) evaluates to true. So the "body" (in this case the print statement) would execute

# What happens if the if statement evaluates to false?
# Well, don't fear, you can have an "elif" statement that runs when the if's boolean condition is false
# Example:
if ( x > y ) : # since condition is false, the if statement's body is skipped and the program moves on
  print("x is greater than y")
elif ( x < y ) : # program goes to elif statement. Since condition is true, body is executed.
  print("x is less than y")

# How about if both the "if" condition and the "elif" condition evaluate to false?
# Never fear! We have "else" statements. You can think of it as a statement that ensures that its body will run if the other two are false. 
# Example:
if ( x == y ) :
  print("x is equal to y")
elif( x < y ) : 
  print("x is less than y")
else: 
  print("x is greater than y")
# Since the if and elif conditions evaluate to false, the program will go to the else statement and immediately run the body. 

# Note: elif and else can't be by themselves. There must be an if statement with them.
#        Also, you don't need an elif and else statement. You can just have an if statement and your program will run fine. 


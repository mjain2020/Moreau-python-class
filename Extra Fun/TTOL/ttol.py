#   __    __           ___
#  /\ \__/\ \__       /\_ \
#  \ \ ,_\ \ ,_\   ___\//\ \
#   \ \ \/\ \ \/  / __`\\ \ \
#    \ \ \_\ \ \_/\ \L\ \\_\ \_
#     \ \__\\ \__\ \____//\____\
#      \/__/ \/__/\/___/ \/____/
#
# Description: A simple game of Two Truths and a Lie with modular truths and lies using its own handler!
#              You only need to run one command to play (play()), and follow the command prompt to start!
#              A file will be generated in the same directory and that will contain your info so you can share with others!
# Author: Anish Govind
# GitHub: https://github.com/generaldefence
# Dependencies: Pickle
# 
# Comments provided to help new Python learners understand

import pickle  # Pickle essentially obscures data we give it until later need

def store_info(path_name="ttol.bin",statements=3, num_false=1):  # Handler to pickle some data to use later
    if statements < 2: # Lets not play a game with only 1 correct answer :D
        return print("You need to have a minimum of 2 statements!")
    elif num_false < 1: # I would also like to have a game with at least 1 lie :D
        return print("You need to have a minimum of 1 lie!")
    elif num_false == statements: # Don't want the people having the same amount of truths as well as lies
        return print("You can't have all the statements become lies... what's the fun in that?")
    data = {"false_statements": num_false} # Dictionary to hold our string then our bool. Has this given so that we can track how many falses are wanted
    num_true = statements-num_false # Number of truths we want
    def get_boolean(): # Handler to get a boolean value from an input we will use later on
        true_keywords = ["True", "true", "1", "T", "t"] # List of all the acceptable values for true
        false_keywords = ["False", "false", "0", "F", "f"] # List of all the acceptable values for false
        x = input("Is this True or False?\n> ") # Ask for true or false
        while x not in true_keywords + false_keywords: # If the input doesn't match what I want in the list, keep asking
            print("Please type a boolean value!")
            x = input(f"Is this True or False?\n> ")            
        if x.lower().strip() in true_keywords: # Basic assignment to get a proper boolean value
            return True
        elif x.lower().strip() in false_keywords:
            return False
    for i in range(0, statements): # Loop to start asking for the statements
        a = input(f"What is the #{i+1} statement? ({num_false} lies left)\n> ") # Basic input with pretty text
        x = get_boolean() # This is where we used the above function to get a boolean value
        if x:             # This statement here makes sure that we don't go under the amount of trues and falses we want
            num_true -= 1 # Simply: If I said a true statement, then subtract one from the total of trues available, and same for false
        else:
            num_false -= 1
        if num_true < 0: # If we do go under the limits, then exit the function
            return print("There are too many true statements!")
        elif num_false < 0:
            return print("There are too many false statements!")
        data[a] = x # Finally store this data in a seperate slot in the dictionary
    if len(data) < statements: # Make sure we didn't type anything twice
        return print("You have too few arguments!\nMaybe you typed the same thing twice?")
    with open(path_name, 'wb') as f: # This is how we pickle the data to another file
        pickle.dump(data, f) # .dump() dumps the dictionary we have into a file that we want
    return print("Stored your information successfully!\n") # Confirmation message that we stored our data


def play(path="ttol.bin"): # Handler to actually play
    # Function to get an integer value from the input() function. This one looks different because it servers more uses
    def get_integer(message, default=None):
        x = input(message) # Get an input
        if not x and default: # If there is no input and we are given a default value, return the default value
            return default
        else:
            try: # See if the person gave us an integer value. If so? Great!
                x = int(x)
            except ValueError: # If they gave something that can't be converted to an integer, run this function again and again
                print("Enter an integer!")
                return get_integer(message)
        return x # Return the integer value
    try: # Let's make this easier for the player so they only have to run 1 function, the play() function
        with open(path, 'rb') as f: # Un-pickle the file we created before
            param = pickle.load(f) # Assign the data (a dictionary) to a variable called param
    except FileNotFoundError: # If there isn't a file with what we want, we will make 1
        print("There doesn't seem to be a file to play with. Let's make one")
        # Run our previous function that pickles some data it'll ask us for, and we use our get_integer() function
        store_info(path_name=path, statements=get_integer("How many statements do you want to play with?\n(Default is 3) > ", default=3),num_false=get_integer("How many lies do you want to say?\n(Default is 1) > ", default=1))
        with open(path, 'rb') as f:  # Un-pickle the file we created before again
            param = pickle.load(f) # Store it to param
    false_statements = param.pop("false_statements") # Let's grab how many false_statements were given and get to work. The .pop() function allows us to return then delete a value from a dictionary. Super useful!
    for i in range(0,len(param)): # This is a for loop to list all the options from our param
        print(f"({i+1}) {list(param.keys())[i]}") # This is just a print statement beautifying the options to make it readable
    def get_answer(single=True): # Function to get the answer from the human after viewing the possible options
        if single: # If we only have 1 false answer, then we will only ask for 1 answer and nothing more
            answer = get_integer(f"Which one is a lie?\n(1-{len(param)}) > ") # Ask for the answer based on the options above
            if answer <= 0 or answer > len(param): # If the answer is 0 or less, it will become negative and break our game, we dont want that
                print("Enter a valid answer choice!")
                return get_answer()  # Re-run the function to get the answer
            return answer-1
        else: # If we have multiple false answers, then we need to get a list
            answer = input(f"Which ones are lies? ({false_statements} lies)\n(Comma seperated from 1-{len(param)}) > ").split(",") # Give us a list of strings without commas
            try:
                answer = [int(i) for i in answer] # Try to integer everything, but if it can't then catch the error
            except ValueError:
                print("Enter a series of comma seperated integers! (e.g. 1,2,3,4)")
                return get_answer(single=False) # Rerun to get a list
            if len(answer) > false_statements: # If there are more answers than false statements, something ain't right
                print(f"Enter exactly {false_statements} values!")
                return get_answer(single=False)
            for i in answer: # Same check like what was for the single answer
                if i <= 0 or i > len(param):
                    print("Enter your answer within the given values!")
                    return get_answer(single=False)
            return answer # Return the list
    if false_statements == 1: # If there is only 1 false answer, then do:
        choice = list(param.values())[get_answer()] # Convert the values from the dictionary into a list of boolean values, then select the answer
        if not choice:  # If the choice gets False, then you win!
            print("You guessed correctly!")
        else:
            print("You didn't guess the right one!")
    else: # If there are more than 1 false statements then:
        answers = get_answer(single=False) # Get the list
        num_correct = 0 # Two placeholder variables to track the number correct and wrong
        num_wrong = 0
        for i in answers: # Loop through the answer list and see which ones are right and which ones are wrong
            if not list(param.values())[i-1]:
                num_correct += 1
            else:
                num_wrong += 1
        # Simple win logic based on incremented numbers
        print(f"You correctly guessed {num_correct} statements as a lie out of {false_statements} meaning you also got {num_wrong} wrong!")
        if num_correct > num_wrong:
            print("You guessed more statements correctly! You win!")
        elif num_correct < num_wrong:
            print("You guessed more statements incorrectly! You lose!")
        else:
            print("You scored exactly the same number wrong and right! Nice job!")
            
play() # Play the game

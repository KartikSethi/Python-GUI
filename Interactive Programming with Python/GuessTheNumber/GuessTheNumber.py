# open the following link to see the code in action: 
# http://www.codeskulptor.org/#user40_3AgulbF31VzXWIn.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

secret_number = 0
num_range = 100
number_of_guesses = 7


# helper function to start and restart the game
def new_game():
    print ""
    global secret_number, num_range
    print "New game. Range is from 0 to",num_range
    print "Number of remaining guesses is",number_of_guesses
    secret_number = random.randrange(0, num_range)
    
    
# defination of event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range, number_of_guesses
    num_range = 100
    number_of_guesses = 7
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, number_of_guesses
    num_range = 1000
    number_of_guesses = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print ""
    global number_of_guesses, secret_number
    guessed_number = int(guess)
    print "Guess was", guessed_number
    number_of_guesses = number_of_guesses-1
    print "Number of remaining guesses is",number_of_guesses
    if number_of_guesses > 0:
        if guessed_number > secret_number:
            print "Lower!"
            
                
        elif guessed_number < secret_number:
            print "Higher!"
        
        else:
            print "Correct!"
            if num_range == 100:
                number_of_guesses = 7
            else:
                number_of_guesses = 10
            new_game()
    elif number_of_guesses == 0:
        #this part of code print appropriate message
        #if the game goes on to upto the last guess  
        
        if guessed_number > secret_number:
            print "Lower!"
            print "You ran out of guesses. The number was", secret_number
            if num_range == 100:
                number_of_guesses = 7
            else:
                number_of_guesses = 10
            new_game()
            
                
        elif guessed_number < secret_number:
            print "Higher!"
            print "You ran out of guesses. The number was", secret_number
            if num_range == 100:
                number_of_guesses = 7
            else:
                number_of_guesses = 10
            new_game()
        
        else:
            print "Correct!"
            if num_range == 100:
                number_of_guesses = 7
            else:
                number_of_guesses = 10
            new_game()
        
        
    

    
# create frame

frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame

frame.add_button("Range is {0, 100)", range100, 200)
frame.add_button("Range is {0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200) 
frame.start()
# call new_game 
new_game()


#Please leave valuable comments.

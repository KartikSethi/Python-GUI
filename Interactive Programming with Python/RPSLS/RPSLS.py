# open the following link to see the code in action: 
# http://www.codeskulptor.org/#user40_lxewj1oqsTfTTyV.py

import random
import simplegui

def name_to_number(name):
    if name == "rock" :
        number = 0
    elif name == "Spock" :
        number = 1
    elif name == "paper" :
        number = 2        
    elif name == "lizard" :
        number = 3
    elif name == "scissors" :    
        number = 4
    else:
        print "Invalid name"
    return number
        

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name= "Spock"
    elif number == 2:
        name= "paper"
    elif number == 3:
        name= "lizard"
    elif number == 4:
        name= "scissors"
    else:
        print "Invalid number"
    return name
    

def rpsls(player_choice):
    print "Player chooses "+player_choice
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0,5)
    
    comp_choice = number_to_name(comp_number)
    print "Computer chooses "+comp_choice
    
    num = (player_number - comp_number) % 5
    
    if (num == 1) or (num == 2):
        print "Player wins!"
    elif (num == 3) or (num == 4):
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    print ""
    print ""

def rock():
    rpsls("rock")
def spock():
    rpsls("Spock")
def paper():
    rpsls("paper")
def lizard():
    rpsls("lizard")
def scissors():
    rpsls("scissors")
# create frame

frame = simplegui.create_frame("RPSLS", 300, 300)

# register event handlers for control elements and start frame

frame.add_button("Rock", rock, 200)
frame.add_button("Spock", spock, 200)
frame.add_button("Paper", paper, 200)
frame.add_button("Lizard", lizard, 200)
frame.add_button("Scissors", scissors, 200)
frame.start()    

"""rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
"""
#Please do leave valuable comments .



# open the following link to see the code in action: 
# http://www.codeskulptor.org/#user42_IgdUXZzIpIfFhuY_1.py

# implementation of card game - Memory

import simplegui
import random

counter = 0
choice1 = -1
choice2 = -1
list1 = range(8)
list2 = range(8)
list2.extend(list1)
state = 0
# exposed list containing the values, True or False for indices of list2
exposed = [False] * 16




# helper function to initialize globals
def new_game():
    global state, counter
    state = 0
    counter = 0
    random.shuffle(list2)
    for i in range(0, 16):
        exposed[i] = False
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, counter, choice1, choice2
    #print state
    index = pos[0] // 50
    if exposed[index]:
        return
    else:
        #print "You clicked on the card at index",index
        exposed[index] = True
        if state == 0:
            state = 1
            choice1 = index
            #print "Choice1=",choice1
        elif state == 1:
            state = 2
            choice2 = index
            counter = counter + 1
        else:
            state = 1
            if list2[choice1] != list2[choice2]:
                    exposed[choice1] = False
                    exposed[choice2] = False                
            choice1 = index
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    pass
    for i in range(15):
        canvas.draw_line((50 * (i+1), 0), (50 * (i+1), 100), 1, 'Blue')
    
    for i in range(1, 17):
        card_pos = [50 * i - 35, 63]
        if exposed[i-1] == True:
            canvas.draw_text(str(list2[i-1]), card_pos, 50, 'White', 'serif')
        else:
            canvas.draw_polygon([[50 * (i-1),0], [50 * i, 0], [50 * i, 100], [50 * (i-1), 100]], 1, 'Blue', 'Red')
        label.set_text("Turns = " + str(counter))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
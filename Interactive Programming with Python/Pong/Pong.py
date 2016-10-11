# open the following link to see the code in action: 
# http://www.codeskulptor.org/#user42_5sVKes1nbMAhDAh_0.py

# Implementation of classic arcade game Pong

"""
    Controls:
    1. Arrow keys for player one
    2. 'W' and 'S' for player two 
"""


import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120.0 / 60.0, 240.0 / 60.0), -random.randrange(60.0 / 60.0, 180.0 / 60.0)]
    else:
        ball_vel = [-random.randrange(120.0 / 60.0, 240.0 / 60.0), -random.randrange(60.0 / 60.0, 180.0 / 60.0)]
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos, paddle2_pos = (HEIGHT - PAD_HEIGHT)/2, (HEIGHT - PAD_HEIGHT)/2
    paddle1_vel = paddle2_vel = 0
    score1, score2 = 0, 0
    spawn_ball(True)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "white")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "white")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "white")
        
    # update ball and determine whether paddle and ball collide and calculate the scores
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos and  ball_pos[1] <= (paddle1_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball(True)
            score2 += 1
    if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if  ball_pos[1] >= paddle2_pos and  ball_pos[1] <= (paddle2_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball(False)
            score1 += 1
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "white", "white")
    
    # update paddle's vertical position, keep paddle on the screen
    new_position1 = paddle1_pos + paddle1_vel
    new_position2 = paddle2_pos + paddle2_vel
    if new_position1 >= 0 and  new_position1 <= HEIGHT - PAD_HEIGHT:
        paddle1_pos = new_position1
    if new_position2 >= 0 and new_position2 <= HEIGHT - PAD_HEIGHT:
        paddle2_pos = new_position2   
    
    # draw paddles
    canvas.draw_line([PAD_WIDTH/2, paddle1_pos],[PAD_WIDTH/2, paddle1_pos+PAD_HEIGHT], PAD_WIDTH, "white")
    canvas.draw_line([WIDTH - PAD_WIDTH/2, paddle2_pos],[WIDTH- PAD_WIDTH/2, paddle2_pos+PAD_HEIGHT], PAD_WIDTH, "white")   
    
    # draw scores
    canvas.draw_text(str(score1), (180, 50), 50, "White", "monospace")
    canvas.draw_text(str(score2), (400, 50), 50, "White", "monospace")
def keydown(key):
    constant_paddle_vel = 4
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -constant_paddle_vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = constant_paddle_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -constant_paddle_vel  
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = constant_paddle_vel
     
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0   
def restart():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 200)


# start frame
new_game()
frame.start()

# open the following link to see the code in action: 
# http://www.codeskulptor.org/#user40_hFHKfsG3abrG28g.py

# template for "Stopwatch: The Game"
import simplegui
# define global variables
counter = 0
attempts = 0
wins = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = str(t // 600)
    b = str((((t // 10) % 60) // 10))
    c = str((((t // 10) % 60) % 10))
    d = str(t % 10)
    return a + ":" + b + c + "." + d    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
     timer.start()
    
def stop():
    global attempts, wins
    attempts = attempts + 1
    if counter % 10 == 0:
        wins = wins + 1
    timer.stop()
    
def reset():
    global attempts, wins, counter
    counter = 0
    attempts = 0
    wins = 0
    timer.stop()
    
def result():
    global wins, attempts
    wins_as_a_string = str(wins)
    attempts_as_a_string = str(attempts)
    return wins_as_a_string + "/" + attempts_as_a_string

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter = counter + 1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), (40, 115), 55, "white",  "monospace")
    canvas.draw_text(result(), (150, 40), 40, "green",  "sans-serif")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",250,200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)


# start frame
frame.start()


# Please leave valuable comments.
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "blue"
score = 0
font_setup = ("Arial", 20, "normal")

#timer set up
timer = 30
counter_interval = 1000
timer_up = False

#-----initialize turtle-----
score_writer = trtl.Turtle()
score_writer.penup()
box_turtle = trtl.Turtle()
box_turtle.penup()
box_turtle.speed(0)
painter = trtl.Turtle()
painter.shape("circle")
painter.color(spot_color)
painter.shapesize(2)
painter.penup()

countdown = trtl.Turtle()
countdown.hideturtle()

countdown_box = trtl.Turtle()
countdown_box.speed(0)
countdown_box.hideturtle()

#-----game functions--------
#get a score boost, move the turtle randomly
def spot_clicked(x, y):
    change_position()
    update_score()
    countdown_function()

def change_position():
    painter.teleport(rand.randint(-360, 300), rand.randint(-360, 332))

def update_score():
    #include global score
    global score
    #increment the score by 1
    score += 1
    #remove previous score
    score_writer.clear()
    #print the score
    score_writer.pendown()
    score_writer.write(score, font=font_setup)

def score_box():
    #setup location and pendown
    box_turtle.goto(275, 355)
    box_turtle.pendown()

#draw the box
    for sides in range(2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(25)
        box_turtle.left(90)
#set up the score_writer in a position to write the score
    score_writer.penup()
    score_writer.goto(300, 350)

def box_countdown():
    countdown_box.teleport(-357, 355)
    for sides in range(2):
        countdown_box.forward(135)
        countdown_box.left(90)
        countdown_box.forward(25)
        countdown_box.left(90)

def countdown_function():
    countdown.teleport(-350, 350)
    global timer, timer_up
    countdown.clear()
    if timer <= 0:
        countdown.write("Time's Up!", font=font_setup)
        timer_up = True
    else:
        countdown.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        countdown.getscreen().ontimer(countdown_function, counter_interval)


#hide the turtles
score_writer.hideturtle()
box_turtle.hideturtle()

#-----events----------------
painter.onclick(spot_clicked)

score_box()

box_countdown()

#set up the screen
wn = trtl.Screen()
wn.ontimer(countdown_function, counter_interval)
wn.mainloop()
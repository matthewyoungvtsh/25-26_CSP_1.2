#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "blue"
score = 0
font_setup = ("Arial", 20, "normal")

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

#-----game functions--------
#get a score boost, move the turtle randomly
def spot_clicked(x, y):
    change_position()
    update_score()

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

#hide the turtles
score_writer.hideturtle()
box_turtle.hideturtle()

#-----events----------------
painter.onclick(spot_clicked)

score_box()

#set up the screen
wn = trtl.Screen()
wn.mainloop()
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "blue"
score = 0

#-----initialize turtle-----
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
    painter.teleport(rand.randint(-360, 360), rand.randint(-360, 300))

def update_score():
    #include global score
    global score
    #increment the score by 1
    score += 1
    #print the score
    print(score)

import turtle as trtl
score_writer = trtl.Turtle()
score_writer.teleport(0, 310)
score_writer.width(5)
score_writer.forward(60)
score_writer.left(90)
score_writer.forward(60)
score_writer.left(90)
score_writer.forward(120)
score_wr

#-----events----------------
painter.onclick(spot_clicked)

#set up the screen
wn = trtl.Screen()
wn.mainloop()
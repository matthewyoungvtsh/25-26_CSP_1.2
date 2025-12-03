# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "blue"

#-----initialize turtle-----
painter = trtl.Turtle()
painter.shape("circle")
painter.color(spot_color)
painter.shapesize(2)
painter.penup()

#-----game functions--------
#get a score boost, move the turtle randomly
def spot_clicked(x, y):
    painter.teleport(rand.randint(-320, 320), rand.randint(-320, 320))

#-----events----------------
painter.onclick(spot_clicked)

#set up the screen
wn = trtl.Screen()
wn.mainloop()
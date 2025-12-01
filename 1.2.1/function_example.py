# Goal: to draw squares using turtle

#import turtle
import turtle as trtl
painter = trtl.Turtle()

def drawSquare():
    for sides in range(4):
        painter.forward(30)
        painter.right(90)

drawSquare()
painter.forward(40)
drawSquare()

for squares in range(5):
    drawSquare()
    painter.forward(60)

wn = trtl.Screen()
wn.mainloop()
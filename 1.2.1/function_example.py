# Goal: to draw squares using turtle

#import turtle
import turtle as trtl
painter = trtl.Turtle()

def drawSquare(length):
    for sides in range(4):
        painter.forward(length)
        painter.right(90)

drawSquare(62)
painter.forward(40)
drawSquare(41)

wn = trtl.Screen()
wn.mainloop()
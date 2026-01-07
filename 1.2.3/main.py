#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
wn.tracer(False)
apple.penup()
drawn_letter = trtl.Turtle()

import random as rand

alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = rand.randint(0, 23)
letter = int(alphabet_list)

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_letter("letter", active_apple)
  wn.tracer(True)
  wn.update()


def draw_letter(letter, active_apple):
    drawn_letter.teleport(0, 400)
    drawn_letter.write("letter", font=("Arial", 60, "bold"))

def drop_apple():
    wn.tracer(True)
    apple.goto(apple.xcor(), ground_height)
    apple.hideturtle()
    drawn_letter.clear()
    wn.tracer(False)

#-----function calls-----
draw_apple(active_apple)
wn.onkeypress(drop_apple, "letter")

wn.mainloop()
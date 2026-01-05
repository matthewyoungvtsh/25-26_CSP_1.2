#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
letter = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_letter()
  wn.update()

def draw_letter():
    letter.teleport(0, 400)
    letter.shape("a")

def drop_apple():
    apple.goto(apple.xcor(), ground_height)

#-----function calls-----
draw_apple(apple)
wn.onkeypress(drop_apple, "a")

wn.mainloop()
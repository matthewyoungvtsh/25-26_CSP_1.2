#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

letter = ""
current_letter = "a"

screen_width = 400 #width of screen
screen_height = 400 #height of screen
ground_height = -200

apple_letter_x_offset = -25
apple_letter_y_offset = -50

wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
wn.tracer(False)
apple.penup()
drawn_letter = trtl.Turtle()

#import random
import random as rand

#full list of the alphabet
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#-----functions-----

def reset_apple(active_apple):
    # generate random letter and pop that index. the letter popped becomes the letter on the apple
    #get global variable
    global current_letter
    #how many letters are left
    length_of_list = len(alphabet_list)
    if length_of_list != 0:
        index = rand.randint(0, length_of_list)
        #set the random letter to our current letter
        current_letter = alphabet_list.pop(index)
        #Goto: x and y -> randomize each
        #active_apple.goto(rand.randint(-(int(screen_width))/2, (int(screen_width))/2), rand.randint(-(int(screen_height))/2, (int(screen_height))/2))
        active_apple.goto(200, 200)
        draw_apple(active_apple, current_letter)



# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, current_letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(current_letter, active_apple)
  wn.update()

#function to write letter on top of screen
def draw_letter(letter, active_apple):
    drawn_letter.teleport(0, 400)
    drawn_letter.write(current_letter, font=("Arial", 60, "bold"))

#function to drop the apple
def drop_apple():
    wn.tracer(True)
    apple.goto(apple.xcor(), ground_height)
    apple.hideturtle()
    drawn_letter.clear()
    wn.tracer(False)
    reset_apple(apple)

def check_apple_a():
    if(current_letter == "a"):
        drop_apple()

#-----function calls-----
draw_apple(apple, current_letter)
wn.onkeypress(check_apple_a, "a")
wn.onkeypress()

#   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the
# turtle with a new letter selected at random from the list of letters

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple resetting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

wn.listen()
wn.mainloop()
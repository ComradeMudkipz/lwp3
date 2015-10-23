# Chapter 3
# tessTurtle.py - Creates an angle via turtle using user-inputted
# attributes.


import turtle


# Creates screen and user-inputted attributes for turtle
bgColor = input("What color would you like the background? ")
wn = turtle.Screen()
wn.bgcolor(bgColor)
tess = turtle.Turtle()
tessColor = input("What color would you like your turtle? ")
tess.color(tessColor)
tessPen = input("And how wide would you like the trail? ")
tess.pensize(int(tessPen))

# Creates an angle on screen.
tess.forward(50)
tess.left(120)
tess.forward(50)

# Keeps window open until it is closed by user.
wn.mainloop()

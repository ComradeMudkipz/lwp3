# Chapter 3
# turtleInstance.py - Program which uses multiple turtles on screen.


import turtle


# Set up the window environment
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Tess & Alex')

# Create tess and set some attributes
tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(5)

# Create alex
alex = turtle.Turtle()

# Make tess draw equilateral triangle
for i in range(3):
    tess.forward(80)
    tess.left(12)
# Turn tess around
tess.right(180)
# Move her away from the origin
tess.forward(80)

# Make alex draw a square
for i in range(4):
    alex.forward(90)
    alex.left(90)

wn.mainloop()

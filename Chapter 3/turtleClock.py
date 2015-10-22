# Chapter 3
# turtleClock.py - Draws a face of a clock using turtle


import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
tess = turtle.Turtle()
tess.shape('turtle')
tess.color('blue')
tess.left(90)
tess.penup()

for i in range(12):
    tess.forward(200)
    tess.pendown()
    tess.forward(40)
    tess.penup()
    tess.forward(30)
    tess.stamp()
    tess.forward(-270)
    tess.right(30)

wn.mainloop()

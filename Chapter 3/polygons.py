# Chapter 3
# polygons.py - Program that creates an equilateral triangle
# using the turtle module


import turtle


wn = turtle.Screen()
wn.bgcolor('black')

josh = turtle.Turtle()
josh.color('white')
josh.pensize(2)
josh.speed(2)
josh.penup()
josh.forward(-300)
josh.pendown()

# Creates an equilateral triangle
for i in range(3):
    josh.forward(40)
    josh.left(120)

josh.penup()
josh.forward(100)
josh.pendown()

# Creates a square
for j in range(4):
    josh.forward(40)
    josh.left(90)

josh.penup()
josh.forward(120)
josh.pendown()

# Creates a hexagon
for k in range(6):
    josh.forward(40)
    josh.left(60)

josh.penup()
josh.forward(140)
josh.pendown()

# Creates a octagon
for l in range(8):
    josh.forward(40)
    josh.left(45)

wn.mainloop()

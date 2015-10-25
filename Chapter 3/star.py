# Chapter 3
# star.py - Draws a star using turtle.


import turtle
wn = turtle.Screen()
draw = turtle.Turtle()
draw.hideturtle()
draw.speed(1)

angle = [36, 144, 144, 144, 144]
for i in angle:
    draw.left(i)
    draw.forward(100)
wn.mainloop()

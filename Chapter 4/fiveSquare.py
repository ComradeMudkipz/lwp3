# Chapter 4
# fiveSquare.py - Draws five squares using functions and loops.


import turtle

def make_window(color, title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w


def make_turtle(color, size):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t


def draw_square(s):
    for i in range(4):
        josh.forward(s)
        josh.left(90)


wn = make_window("lightgreen", "Five Squares")
josh = make_turtle("hotpink", 3)
josh.speed(2)

for i in range(5):
    draw_square(20)
    josh.penup()
    josh.forward(40)
    josh.pendown()

wn.mainloop()

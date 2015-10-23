# Chapter 4
# prettyPattern.py - Draws a pretty pattern.


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


wn = make_window("lightgreen", "Trippy.")
josh = make_turtle("blue", 3)
josh.speed(5)

x = 0
for i in range(20):
    draw_square(120)
    josh.left(18)

wn.mainloop()

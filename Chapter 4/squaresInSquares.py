# Chapter 4
# squaresInSquares.py - Draws squares with squares within them.


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


def square_reposition(a, b):
    josh.penup()
    josh.right(a)
    josh.forward(b)
    josh.left(a)
    josh.backward(b)
    josh.pendown()


wn = make_window("lightgreen", "Mmm... squares.")
josh = make_turtle("hotpink", 3)
josh.speed(1)

x = 0
for i in range(5):
    x = x + 20
    draw_square(x)
    square_reposition(90, 10)

wn.mainloop()

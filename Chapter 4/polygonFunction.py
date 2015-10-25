# Chapter 4
# polygonFunction.py - Draws a polygon with attributes set in a function.


import turtle

def make_window(color, title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w


def draw_poly(t, n, sz):
    t = turtle.Turtle()
    t.color("hotpink")
    t.pensize(3)
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)


wn = make_window("lightgreen", "OCTAGON!")
draw_poly('josh', 8, 50)

wn.mainloop()

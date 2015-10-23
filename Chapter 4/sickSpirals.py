# Chapter 4
# sickSpirals.py - Draws two spirals that differ only by the angle.
# TODO: INCOMPLETE


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


def draw_spiral(f):
    
    
wn = make_window("lightgreen", "Holy fucking shit")
josh = make_turtle("blue", 3)
josh.speed(5)

for i in range(20):


wn.mainloop()

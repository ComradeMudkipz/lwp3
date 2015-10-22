# Chapter 3
# drunkPirate.py - Program which draws the path of a "drunk pirate."


import turtle
wn = turtle.Screen()
wn.bgcolor('light green')
drunk = turtle.Turtle()
drunk.color('red')
drunk.pensize(3)
path = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in path:
    drunk.left(i)
    drunk.forward(100)

# Print the pirate's heading.
heading = 0
for x in path:
    heading = x + int(heading)

print(heading)
wn.mainloop()

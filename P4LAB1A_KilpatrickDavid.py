# David Kilpatrick
# P4LAB1A
# Turtle Drawing Square and Triangle

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.pensize(4)


# square
side = 0
while side < 4:
    t.forward(100)
    t.right(90)
    side = side + 1

# triangle
side = 0
while side < 3:
    t.forward(100)
    t.right(120)
    side = side + 1

wn.mainloop()

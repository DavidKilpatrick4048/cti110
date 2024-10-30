# David Kilpatrick
# P4LAB1B
# Initials drawn with turtles

import turtle

t = turtle.Turtle()
t.pensize(8)        
t.pencolor("orange")      
t.speed(4)              

# Draw letter D
t.penup()
t.goto(-50, 0)           
t.pendown()
t.circle(80,180)
t.left(90)
t.forward(160)
t.left(90)

# Draw letter K
t.penup()
t.goto(150, 150)           
t.pendown()
t.right(90)
t.forward(200)
t.backward(100)
t.left(45)
t.forward(125)
t.backward(125)
t.left(90)
t.forward(125)

turtle.done()

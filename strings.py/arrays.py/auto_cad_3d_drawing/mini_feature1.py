import turtle

t = turtle.Turtle()

length = 200
width = 120

for i in range(2):
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)

turtle.done()
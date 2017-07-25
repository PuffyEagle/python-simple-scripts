import turtle

window = turtle.Screen()
Turtle = turtle.Turtle()

Turtle.penup()
Turtle.right(90)
Turtle.forward(200)
Turtle.left(90)
Turtle.pendown()

Turtle.fillcolor("green")
Turtle.begin_fill()
for i in range(0,360):
    Turtle.forward(4)
    Turtle.left(1)
Turtle.end_fill()

Turtle.penup()
Turtle.left(90)
Turtle.forward(70)
Turtle.right(90)
Turtle.pendown()

for i in [0,1,2,3,4,5,6,7]:
    Turtle.forward(100)
    Turtle.left(45)
    Turtle.dot()

Turtle.penup()
Turtle.left(90)
Turtle.forward(70)
Turtle.right(90)
Turtle.pendown()

Turtle.fillcolor("red")
Turtle.begin_fill()
for i in [0,1,2,3,4]:
    Turtle.forward(50)
    Turtle.left(72)
Turtle.end_fill()

window.exitonclick()

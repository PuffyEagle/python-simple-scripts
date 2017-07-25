import turtle

wn = turtle.Screen()
wn.bgcolor("black")
alex = turtle.Turtle()
alex.color("blue")
alex.fillcolor("green")
alex.speed(10)

alex.forward(-300)

alex.begin_fill()
for i in range(0,72):
    alex.forward(600)
    alex.left(175)
alex.end_fill()

wn.exitonclick()

import turtle

#Pre: The user needs window.
#Post: Window is created and returned.
def CreateWindow():
    window = turtle.Screen()
    return window

#Pre: A turtle is needed.
#Post: A turtle is created and returned.
def CreateATurtle():
    ATurtle = turtle.Turtle()
    return ATurtle

#Pre: A certain number of rhombuses need to be drawn in certain locations
    #with a turtle.
#Post: All rhombuses that are needed are drawn and moved to their locations.
def DrawAllRhombuses(ATurtle):
    for i in [0,1,2,3,4,5]:
        for i in [0,1,2,3,4,5]:
            DrawOneRhombus(ATurtle)
            TurnMoveATurtle(ATurtle,0,40)
        TurnMoveATurtle(ATurtle,90,40)
        TurnMoveATurtle(ATurtle,0,-240) 

#Pre: The user wants to draw a rhombus with a turtle.
#Post: A rhombus is drawn.
def DrawOneRhombus(ATurtle):
    for NumbofDegrees in [60,120,60,120]:
        ATurtle.forward(20)
        ATurtle.left(NumbofDegrees)

#Pre: A turtle needs to be turned and moved.
#Post: The turtle is turned a specific amount of degrees and moved forward a
        #specific amount.
def TurnMoveATurtle(ATurtle,Degrees,AmountForward):
    ATurtle.penup()
    ATurtle.left(-1*Degrees)
    ATurtle.forward(AmountForward)
    ATurtle.pendown()
    ATurtle.left(Degrees)

#Pre: A dot is needed in the middle of the screen.
#Post: The turtle makes a dot in the middle of the screen.
def MakeDotInMiddle(ATurtle):
    ATurtle.dot()

def main():
    window = CreateWindow()
    ATurtle = CreateATurtle()
    window.bgcolor("lightgreen")
    MakeDotInMiddle(ATurtle)
    TurnMoveATurtle(ATurtle,-90,90)
    TurnMoveATurtle(ATurtle,-180,110)
    DrawAllRhombuses(ATurtle)
    window.exitonclick()

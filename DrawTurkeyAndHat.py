import turtle

#Pre: aTurtle, aColor, and radius exist and are valid.
#Post: A full circle is drawn with a specific color filling.
def drawCircle(aTurtle,aColor,radius,degrees):
    if aColor != "none":
        aTurtle.fillcolor(aColor)
        aTurtle.begin_fill()
        aTurtle.circle(radius,degrees)
        aTurtle.end_fill()
    else:
        aTurtle.circle(radius,degrees)

#Pre: aTurtle, sideLen, and aColor are valid and exist.
#Post: A triangle (the turkey's beak) is drawn.
def drawBeak(aTurtle,sideLen,aColor):
    aTurtle.fillcolor(aColor)
    aTurtle.begin_fill()
    aTurtle.forward(sideLen)
    aTurtle.right(120)
    aTurtle.forward(sideLen)
    aTurtle.right(120)
    aTurtle.forward(sideLen)
    aTurtle.end_fill()

#Pre: aTurtle exists and is valid.
#Post: The turkey's feathers are drawn with different color filling.
def drawFeathers(aTurtle,InitialX,InitialY):
    aTurtle.left(35)
    for aColor in ["orange","yellow","light blue","green","light pink"]:
        moveTurtle(aTurtle,InitialX,InitialY)
        drawOvalShape(25,160,aTurtle,190,aColor)
        aTurtle.right(165)

#Pre: circRadius, AmntFrwd, aTurtle, circDegrees, and aColor all exist and are valid.
#Post: An oval shape (straight line, part of a circle, straight line) is drawn.
def drawOvalShape(circRadius,AmntFrwd,aTurtle,circDegrees,aColor):
    aTurtle.fillcolor(aColor)
    aTurtle.begin_fill()
    aTurtle.forward(AmntFrwd)
    drawCircle(aTurtle,"none",circRadius,circDegrees)
    aTurtle.forward(AmntFrwd)
    aTurtle.end_fill()

#Pre: aTurtle exists and is valid.
#Post: One of the turkey's legs is drawn.
def drawLeg(aTurtle):
    aTurtle.left(50)
    drawOvalShape(8,40,aTurtle,180,"yellow")
    aTurtle.right(90)
    CurrentX,CurrentY = aTurtle.position()
    moveTurtle(aTurtle,CurrentX-8,CurrentY+8)
    drawOvalShape(8,40,aTurtle,180,"yellow")
    aTurtle.right(40)
    drawOvalShape(8,45,aTurtle,180,"yellow")
    drawOvalShape(8,45,aTurtle,180,"yellow")

#Pre: aTurtle,Xcoord, and Ycoord exist and are valid.
#Post: Two turkey legs are drawn.
def drawTurkeyLegs(aTurtle,Xcoord,Ycoord):
    moveTurtle(aTurtle,Xcoord,Ycoord)
    drawLeg(aTurtle)
    CurrentX,CurrentY = aTurtle.position()
    moveTurtle(aTurtle,CurrentX+130,CurrentY)
    aTurtle.left(105)
    drawLeg(aTurtle)

#Pre: aTurtle exists and is valid.
#Post: The problem statement is solved and a turkey is drawn.
def drawTurkey(aTurtle,initialX,initialY):
    drawFeathers(aTurtle,initialX,initialY)

    drawTurkeyLegs(aTurtle,initialX-70,initialY-120)

    aTurtle.right(105)
    aTurtle.color("black")
    moveTurtle(aTurtle,initialX,initialY-110)
    drawCircle(aTurtle,"brown",100,360) #body

    aTurtle.right(100)
    moveTurtle(aTurtle,initialX-10,initialY+80)        #neck
    drawOvalShape(25,100,aTurtle,200,"dark red")

    aTurtle.right(100)
    moveTurtle(aTurtle,initialX,initialY+40)
    drawCircle(aTurtle,"maroon",40,360) #head

    for i in [-15,15]:
        moveTurtle(aTurtle,initialX+i,initialY+88)
        drawCircle(aTurtle,"grey",8,360)    #eye

    moveTurtle(aTurtle,initialX-10,initialY+80)    #beak
    drawBeak(aTurtle,20,"yellow")

#Pre: aTurtle exists and is valid.
#Post: Top of hat is drawn.
def drawTopofHat(aTurtle):
    aTurtle.begin_fill()
    aTurtle.left(5)
    CurrentX,CurrentY = aTurtle.position()
    moveTurtle(aTurtle,CurrentX-30,CurrentY)
    aTurtle.forward(100)
    aTurtle.left(80)
    aTurtle.forward(110)
    aTurtle.left(80)
    aTurtle.forward(100)
    aTurtle.end_fill()
    
#Pre: aTurtle exists and is valid.
#Post: The problem statement is solved and a Pilgrim hat is drawn.
def drawPilgrimHat(aTurtle,initialX,initialY):
    moveTurtle(aTurtle,150,-150)
    drawOvalShape(100,0,aTurtle,190,"black")    #hat bottom

    drawTopofHat(aTurtle)

    FirstPosX,FirstPosY = aTurtle.position()
    aTurtle.color("brown")  #brown buckle strap
    aTurtle.pensize(5)
    SemiCylinderShape(aTurtle,FirstPosX,FirstPosY,18,75,160,20,20,30,205,70,150)

    aTurtle.color("gold")       #buckle
    aTurtle.pensize(8)
    moveTurtle(aTurtle,initialX+80,initialY-20)
    SemiCylinderShape(aTurtle,initialX+80,initialY-20,270,70,50,240,0,40,71,70,50)
                      
    moveTurtle(aTurtle,initialX+80,initialY-45)    #Little buckle knob
    aTurtle.right(35)
    aTurtle.forward(15)


#Pre: aTurtle,xcoord,ycoord,FirstLTurn,radius,degrees,LTurn2,RghtTurn,FrwdAmnt,Left3,radius2,and
    # degrees2 all exist and are valid.
#Post: Part of a cylinder is drawn.
def SemiCylinderShape(aTurtle,xcoord,ycoord,FirstLTurn,radius,degrees,LTurn2,RghtTurn,FrwdAmnt,Left3,radius2,degrees2):
    aTurtle.left(FirstLTurn)
    drawCircle(aTurtle,"none",radius,degrees)
    aTurtle.left(LTurn2)
    aTurtle.forward(FrwdAmnt)
    moveTurtle(aTurtle,xcoord,ycoord)
    aTurtle.right(RghtTurn)
    aTurtle.forward(FrwdAmnt)
    aTurtle.left(Left3)
    drawCircle(aTurtle,"none",radius2,degrees2)



#Pre: aTurtle, xcoord, and ycoord exist and are valid.
#Post: aTurtle is moved to the desired spot.
def moveTurtle(aTurtle,xcoord,ycoord):
    aTurtle.penup()
    aTurtle.goto(xcoord,ycoord)
    aTurtle.pendown()

def main():
    window = turtle.Screen()
    aTurtle = turtle.Turtle()
    aTurtle.shape("blank")
    
    drawTurkey(aTurtle,-150,120)
    aTurtle.right(215)
    drawPilgrimHat(aTurtle,150,-150)
    
    window.exitonclick()

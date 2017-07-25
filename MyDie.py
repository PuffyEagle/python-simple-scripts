# MyDie.py
from random import randrange

class MyDie:

    def __init__(self, sides):  #constructor
        self.sides = sides
        self.value = 1

    def roll(self):             #mutator method
        self.value = randrange(1,self.sides+1)

    def getValue(self):         #accessor method
        return self.value

    def setValue(self, value):  #mutator method
        self.value = value  



def main():
    numsides = getInteger("Enter the number of sides for the die: ")
    #Construct an MyDie object
    die1 = MyDie(numsides)
    
    numrolls = getInteger("Enter the number of rolls: ")
    displayRolls(die1,numrolls)

def getInteger(msg):
    myinput = ""
    while myinput=="":
        try:
            myinput = int(input(msg))
        except ValueError:
            print("Not an integer.")

    return myinput

def displayRolls(dieOne,numrolls):
    for i in range(numrolls):
        #Roll the die object
        rollDie(dieOne)
        #Display the value of the die
        displayDie(dieOne)
    print()
    
def rollDie(dieA):
    dieA.roll()

def displayDie(dieB):
    print(dieB.getValue(), end=" ")

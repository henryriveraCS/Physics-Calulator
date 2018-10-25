
# Written by HenryRivera.CS
"""
This program will calculate the addition and subtraction of vectors alongside
It can also tell you the quadrant of said vector, and x/y components of the vector.
"""
# a basic x,y input for one vector at a time
import math

class Vector:
    def magnitude(self, xpos, ypos):
        magResult = math.sqrt(ypos**2 +xpos**2)
        roundingMag = round(magResult, 2)
        return self, roundingMag

    def angle(self, xpos, ypos):
        radianResult = math.atan(ypos/xpos)
        degreeResult = math.degrees(radianResult)
        roundingAngle = round(degreeResult, 2)

        return self, roundingAngle

    def xcomp(self, magnitood, angle):
        xformula = (magnitood * math.cos(math.radians(angle)))
        return self, xformula

    def ycomp(self, magnitood, angle):
        yformula = (magnitood * math.sin(math.radians(angle)))
        return self, yformula

    def quadrant(self, angle):
        if angle > 0  and angle < 90:
            return self, "Quadrant 1"
        elif angle > 90 and angle < 180:
            return self, "Quadrant 2"
        elif angle > 180 and angle < 270:
            return self, "Quadrant 3"
        elif angle > 270 and angle < 360:
            return self, "Quadrant 4"
        else:
            print("The vector is on an axis"
            )
    def addingVec(self, x1, y1, x2, y2):
        x3 = x1 + x2
        y3 = y1 + y2
        return self, x3, y3

    def subtractingVec(self, x1, y1, x2, y2):
        x3 = x1 - x2
        y3 = y1 - y2
        return self, x3, y3

def main():
    print("Welcome to Henry's Vector Calculator! These are the options:")
    print("1) Find magnitude of a vector.")
    print("2) Find angle of a vector.")
    print("3) Find quadrant of a vector.")
    print("4) Find X and Y components of a vector.")
    print("5) Add vectors.")
    print("6) Subtract vectors")
    userInput = int(input("Which are you trying to do?(Numbers only)"))

    """ possible inputs
    nameInput = str(input('Name of vector?'))
    xinput = int(input("X component value: "))
    yinput = int(input("Y component value: "))
    x2input = int(input("X2 component value: "))
    y2input = int(input("Y2 component value: "))
    angleinput = int(input("Angle value: "))
    magnitudeinput = int(input("magnitude value: "))
    """

    if userInput == 1: # magnitude of a vector
        nameInput = str(input('Name of vector?'))
        xinput = int(input("X component value: "))
        yinput = int(input("Y component value: "))
        print(Vector.magnitude(nameInput, xinput, yinput))
    elif userInput == 2: # find angle of a vector
        nameInput = str(input('Name of vector?'))
        xinput = int(input("X component value: "))
        yinput = int(input("Y component value: "))
        print("Your angle is: ")
        print(Vector.angle(nameInput, xinput, yinput))
    elif userInput == 3: # quadrant of vector
        nameInput = str(input('Name of vector?'))
        angleinput = int(input("Angle value: "))
        print("Your quadrant is: ")
        print(Vector.quadrant(nameInput, angleinput))
    elif userInput == 4: # finding x+y
        nameInput = str(input('Name of vector?'))
        angleinput = int(input("Angle value: "))
        magnitudeinput = int(input("magnitude value: "))
        print("X magnitude:", Vector.xcomp(nameInput, magnitudeinput, angleinput))
        print("Y magnitude:",  Vector.ycomp(nameInput, magnitudeinput, angleinput))
    elif userInput == 5: # adding vectors
        nameInput = str(input('Name of vector?'))
        xinput = int(input("X1 component value: "))
        yinput = int(input("Y1 component value: "))
        x2input = int(input("X2 component value: "))
        y2input = int(input("Y2 component value: "))
        print(Vector.addingVec(nameInput, xinput, yinput, x2input, y2input))
    elif userInput == 6: # subtracting vectors
        nameInput = str(input('Name of vector?'))
        xinput = int(input("X1 component value: "))
        yinput = int(input("Y1 component value: "))
        x2input = int(input("X2 component value: "))
        y2input = int(input("Y2 component value: "))
        print(Vector.subtractingVec(nameInput, xinput, yinput, x2input, y2input))
    else:
        print("Sorry! Only numbers 1-6!")

main()

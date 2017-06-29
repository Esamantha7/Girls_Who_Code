from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
def drawShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        turtle.forward(50)
        turtle.right(angle)
        drawnSides+=1

#########################################
        #Running Program
another = True

sam = Turtle()
sam.pencolor("Purple")
sam.turtlesize(2,2)
sam.pensize(5)
sam.pendown()

while another == True:
    print("How many sides do you want your shape to have?")
    numSides = int(input())
    print("What color do you want your shape to be?")
    chosenColor = input()
    drawShape(sam,numSides,chosenColor)

    print("Do you want to draw another shape?")
    answer = input()
    if(answer == "no"):
        another = False



# Close window on click.
exitonclick()


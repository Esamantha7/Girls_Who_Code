from turtle import*
import math

#setting up screen size
setup(700,500)




#FUNCTIONS
def whileDrawShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        turtle.forward(50)
        turtle.right(angle)
        drawnSides += 1
def forDrawShape(turtle,sides,color):
    turtle.pencolor(color)
    angle = 360/sides

    for s in range(sides):
        turtle.forward(50)
        turtle.right(angle)
    

    

#RUNNING CODE
Anah = Turtle() #creates turtle
Anah.turtlesize(2,2) #makes turtle larger
Anah.pensize(5) #makes pen larger
Anah.pendown()

another = True

while another ==True:
    print("How many sides do you want your shape to have?")
    numSides = int(input())

    print("What color do you want your shape to be?")
    chosenColor = input()

    forDrawShape(Anah,numSides,chosenColor)

    print("Do you want to draw another shape?")
    answer = input()

    if (answer == "no"):
        another = False
    if (answer == "yes"):
        Anah.penup()
        Anah.forward(90)
        Anah.pendown()


#whileDrawShape(Anah,4,"green")
#Anah.penup()
#Anah.pendown()

#closes the window turtle on click
exitonclick()

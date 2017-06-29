from turtle import*
import math

setup(800,800)


def fordrawFlower(turtle,color,size):
    turtle.pencolor(color)
    turtle.circle(size)
flower = Turtle()
flower.pendown()
##drawFlower(flower,"black",50)
##flower.right(40)
##drawFlower(flower,"black",50)

def drawFlower(flower,color,size):
    flower.pencolor(color)
    flower.circle(size)

print("What color do you want?")
chosenColor = input()

print("How big do you want your petals to be?")
numSize = int(input())

print("How many circles do you want your flower to have?")
petals = int(input())
for i in range(petals):
    flower.right(30)
    drawFlower(flower,color,size):

fordrawFlower(flower,chosenColor,numSize)


exitonclick()

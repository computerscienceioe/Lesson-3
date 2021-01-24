import turtle
from random import randint

def shape(sides):
  for i in range(sides):
    turtle.forward(120/sides)
    turtle.right(360/sides)

def startPosition():
  turtle.penup()
  turtle.goto(-200,200)
  turtle.pendown()

def moveToNextShape():
  turtle.setheading(0)
  turtle.penup()
  turtle.forward(60)
  turtle.pendown()

def moveToNextRow():
  turtle.setheading(-90)
  turtle.penup()
  turtle.forward(50)
  turtle.setheading(0)
  turtle.backward(360)
  turtle.pendown()


turtle.speed(10)
startPosition()

for j in range(6):
  for i in range(6):  
    turtle.color(randint(0,255), randint(0,255), randint(0,255))
    turtle.begin_fill()
    shape(randint(3,11))
    turtle.end_fill()
    moveToNextShape()
  moveToNextRow()

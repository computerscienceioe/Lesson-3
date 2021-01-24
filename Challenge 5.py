import turtle
from random import randint

def randomColour():
  turtle.color(randint(0,255), randint(0,255), randint(0,255))

def triangle():
  for i in range(3):
    turtle.forward(120/3)
    turtle.left(360/3)

def hexagonPattern():
  for i in range(6):
    randomColour()
    turtle.begin_fill()
    triangle()
    turtle.end_fill()
    turtle.forward(40)
    turtle.left(60)

def randomPosition():
  turtle.penup()
  turtle.goto(randint(-150,150), randint(-150,150))
  turtle.pendown()



turtle.speed(0)

for i in range(10):
  randomPosition()
  hexagonPattern()



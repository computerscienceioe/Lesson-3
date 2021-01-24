import turtle

def square():
  for i in range(4):
    turtle.forward(30)
    turtle.right(90)

def triangle():
  for i in range(3):
    turtle.forward(40)
    turtle.right(120)

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
  for i in range(3):  
    square()
    moveToNextShape()
    triangle()
    moveToNextShape()
  moveToNextRow()

import turtle

def square():
  for i in range(4):
    turtle.forward(30)
    turtle.right(90)

def triangle():
  for i in range(3):
    turtle.forward(40)
    turtle.right(120)

for i in range(2):  
  square()
  turtle.penup()
  turtle.forward(60)
  turtle.pendown()
  triangle()
  turtle.penup()
  turtle.forward(60)
  turtle.pendown()

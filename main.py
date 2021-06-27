
import turtle

def shape(size,sides):

  for x in range(sides):

    turtle.forward(size)
    turtle.left(360/sides)

shape(1,1)
import turtle
import random

cheese = turtle.Turtle()

# circle #1


turtle.colormode(255)
r = random.randint(255,255)
g = random.randint(0,0)
b = random.randint(0,0)
cheese.color(r,g,b)


cheese.penup()
#cheese will make a circle
cheese.forward(100)
cheese.left(90)
cheese.pendown()
for i in range (360): 
	cheese.forward(1)
	cheese.right(1)
#cheese will move to make the next circle
cheese.penup()
cheese.left(90)
cheese.forward(10)


# circle #2


turtle.colormode(255)
r = random.randint(0,0)
g = random.randint(0,0)
b = random.randint(0,0)
cheese.color(r,g,b)


#cheese will make a circle
cheese.forward(100)
cheese.left(90)
cheese.pendown()
for i in range (360): 
	cheese.forward(1)
	cheese.left(1)
#cheese will move to make the next circle
cheese.penup()
cheese.right(90)
cheese.forward(10)

# circle #3

turtle.colormode(255)
r = random.randint(0,0)
g = random.randint(0,0)
b = random.randint(255,255)
cheese.color(r,g,b)


#cheese will make a circle
cheese.forward(100)
cheese.left(90)
cheese.pendown()
for i in range (450): 
	cheese.forward(1)
	cheese.left(1)
#cheese will move to make the next circle
cheese.penup()
cheese.right(90)
cheese.forward(10)

# circle #4

turtle.colormode(255)
r = random.randint(255,255)
g = random.randint(255,255)
b = random.randint(0,0)
cheese.color(r,g,b)

cheese.pendown()
for i in range (540):
	cheese.forward(1)
	cheese.left(1)
cheese.penup()
cheese.left(90)
cheese.forward(10)
cheese.right(90)

# circle #5

turtle.colormode(255)
r = random.randint(0,0)
g = random.randint(255,255)
b = random.randint(0,0)
cheese.color(r,g,b)

cheese.pendown()
for i in range (540):
	cheese.forward(1)
	cheese.right(1)

cheese.penup()
cheese.forward(300)

turtle.done()
#This first activity is designed 
#to get you started writing some simple programs in Python 
#using the turtle graphics system. 
#There is a chapter on turtle graphics that will go into more detail 
#but for today you can have some fun and do a lot 
#by simply modifying the following example:

import turtle

my_turtle = turtle.Turtle()   # create a turtle
my_turtle.color('green')      # set the color
my_turtle.forward(50)         # draw a green line of length 50
my_turtle.up()                # lift up the tail
my_turtle.forward(50)         # move forward 50 without drawing
my_turtle.right(90)           # change direction to the right, left works too
my_turtle.down()              # put the tail down
my_turtle.backward(100)       # draw a green line 100 units long



#Using the above example to get started create a turtle and draw an interesting picture.
import turtle

my_turtle = turtle.Turtle()   # create a turtle
my_turtle.color('green')      # set the color
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(45)
my_turtle.back(20)
my_turtle.forward(20)
my_turtle.left(90)
my_turtle.forward(20)
my_turtle.back(20)
my_turtle.up()
my_turtle.right(135)
my_turtle.forward(20)
my_turtle.down()
my_turtle.left(90)
my_turtle.forward(20)
my_turtle.right(90)
my_turtle.forward(20)
my_turtle.right(90)
my_turtle.forward(40)
my_turtle.right(90)
my_turtle.forward(20)
my_turtle.right(90)
my_turtle.forward(20)

#How many trees are in the state of Washington?
acresOfWashington = 45663000
estimatedPercentTreeCovered = 0.6
acresOfStateWithTrees = acresOfWashington * estimatedPercentTreeCovered

estimatedNumberOfTreesPerAcre = 40

answer = estimatedNumberOfTreesPerAcre * acresOfStateWithTrees
answer = round(answer)

print(answer)


#How many handshakes for all the people in your class?
people = input("How many people are there?")
people = int(people)

output = 0

for x in range(people):
    output = output + x
    
print(output)



#Ask the user for a side length and then draw a triangle.
length = input("Length of side?")
length = int(length)

import turtle

my_turtle = turtle.Turtle()   # create a turtle
my_turtle.color('green')      # set the color
my_turtle.forward(length)
my_turtle.left(120)
my_turtle.forward(length)
my_turtle.left(120)
my_turtle.forward(length)


#Ask the user for a side length and then draw a square
length = input("Length of side?")
length = int(length)

import turtle

my_turtle = turtle.Turtle()   # create a turtle
my_turtle.color('green')      # set the color
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)


#Ask the user for a side length and then draw an octagon (8-sided)
length = input("Length of side?")
length = int(length)

import turtle

my_turtle = turtle.Turtle()   # create a turtle
my_turtle.color('green')      # set the color
my_turtle.forward(length)         # draw a green line of length 50
my_turtle.left(45)
my_turtle.forward(length)         # draw a green line of length 50
my_turtle.left(45)
my_turtle.forward(length)         # draw a green line of length 50
my_turtle.left(45)
my_turtle.forward(length)         # draw a green line of length 50
my_turtle.left(45)
my_turtle.forward(length)         # draw a green line of length 50
my_turtle.left(45)
my_turtle.forward(length)         # draw a green line of length 50
my_turtle.left(45)
my_turtle.forward(length)         # draw a green line of length 50
my_turtle.left(45)
my_turtle.forward(length)         # draw a green line of length 50


#Last question redone to be scalable
length = input("Length of side?")
length = int(length)

sides = input("how many sides?")
sides = int(sides)

exteriorAngle = 360 / sides

import turtle

my_turtle = turtle.Turtle()   # create a turtle
my_turtle.color('green')      # set the color
for x in range(sides):
    my_turtle.forward(length)
    my_turtle.left(exteriorAngle)
    
    
#Ask the user for a radius and then draw a circle with that radius.
radius = input("length of radius?")
radius = int(radius)

sides = input("how many sides?")
sides = int(sides)

exteriorAngle = 360 / sides

length = (2 * 3.1415 * radius) / sides

import turtle

my_turtle = turtle.Turtle()   # create a turtle
my_turtle.color('green')      # set the color
for x in range(sides):
    my_turtle.forward(length)
    my_turtle.left(exteriorAngle)
    
    
#Ask the user for a radius and then draw a circle with that radius, but make the center of the circle at the current location of the turtle.
radius = input("length of radius?")
radius = int(radius)

#sides = input("how many sides?")
#sides = int(sides)

sides = 120

exteriorAngle = 360 / sides

length = (2 * 3.1415 * radius) / sides

import turtle

my_turtle = turtle.Turtle()   # create a turtle
my_turtle.color('green')      # set the color
my_turtle.up()
my_turtle.right(90)
my_turtle.forward(radius)
my_turtle.left(90)
my_turtle.down()
for x in range(sides):
    my_turtle.forward(length)
    my_turtle.left(exteriorAngle)

    

#Write a program to draw a face of a clock that looks something like this:
import turtle
wn = turtle.Screen()
wn.bgcolor("#9ced91")
buster = turtle.Turtle()
buster.pensize(2)
buster.color("blue")
buster.speed(10)
buster.shape("turtle")
buster.penup()
for x in range(12):
    buster.forward(75)
    buster.pendown()
    buster.forward(10)
    buster.penup()
    buster.forward(15)
    buster.stamp()
    buster.backward(100)
    buster.left(30)

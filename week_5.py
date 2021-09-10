#In Robert McCloskey’s book Make Way for Ducklings, 
#the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. 
#This loop tries to output these names in order.

#Of course, that’s not quite right because Ouack and Quack are misspelled. Can you fix it?

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if (p == "O" or p == "Q"):
        p += "u"
    print(p + suffix)

#Get the user to enter some text and print it out in reverse order.

input = input("Type something that will be reversed")
output = ""
for index in range(len(input)):
    index += 1
    index *= -1
    output += input[index]
print(output)

#Write a program that uses a for loop to print
#One of the months of the year is January
#One of the months of the year is February
#One of the months of the year is March
#etc …

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in months:
    print("One of the months of the year is " + month)

#Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
#Write a loop that prints each of the numbers on a new line.
#Write a loop that prints each number and its square on a new line.
list = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for item in list:
    print(item)
for item in list:
    print(item)
    print(item**2)
    
#Write a program that asks the user for the number of sides, 
#the length of the side, the color, and the fill color of a regular polygon. 
#The program should draw the polygon and then fill it in.
sides = int(input("how many sides?"))
length = int(input("how long are the sides?"))
color = input("what color are the sides?")
fill = input("what color is the fill?")


my_turtle = turtle.Turtle()
my_turtle.color(color)
my_turtle.fillcolor(fill)
my_turtle.begin_fill()
for side in range(sides):
    my_turtle.forward(length)
    my_turtle.left(360/sides)
my_turtle.end_fill()



#A drunk pirate makes a random turn and then takes 100 steps forward, 
#makes another random turn, takes another 100 steps, turns another random amount, etc. 
#A social science student records the angle of each turn before the next 100 steps are taken. 
#Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) 
#Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading. 
#Assume that the turtle originally has a heading of 0 and accumulate the changes in heading to print out the final. 
#Your solution should work for any sequence of experimental data.

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

import turtle

heading = 0;

pirate = turtle.Turtle()
pirate.speed(8)
for turn in turns:
    pirate.left(turn)
    pirate.forward(100)
    heading += turn
print(heading % 360)

#could also just use print(pirate.heading())


#Write a program that uses the turtle module and a for loop to draw something. 
#It doesn’t have to be complicated, but draw something different than we have done in the past. 
#(Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. 
#Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)

import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
turn = 50
length = 1
for x in range(250):
    my_turtle.left(turn % 360)
    turn *= -3
    my_turtle.forward(length)
    length += 2

#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

Turtle()

# add a thick line 
up()
goto(100,-100)
down()
pensize(10)
goto(375,-375)

#go home and move to new space
up()
home()
forward(150)

#add a circle
shape('circle')
down()
stamp()

# move to new space
up()
left(90)
forward(100)
down()

# add a polygon (4 sides)
shape('square')

# change color for extra credit 
color(255,0,0)
stamp()

# go home
up()
home()

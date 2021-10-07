#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:23:14 2021

@author: sazamore
Random walk animation

This code demonstrates how to animate a random walk using turtle.
Random walks are a great approximation for diffusive behaviors (spreading out naturalistically)
Really fun to use with a large number of small turtles!
This movement can be used in combination with other movements.
This code is in function-based form
"""

import turtle 
import time, random # to control framrate and add randomness
turtle.colormode(255)
turtle.tracer(0) #turn off animation

running = True # control the animation loop
counter = 0 # "timer" to stop the code
rw = turtle.Turtle(shape='circle') # random walk

def randomWalk(turt, step=5,anglerange=180):
    """This function randomly steps a turtle (turt) to create a random
    walk. 
    Arguments:
        turt (turtle)- a turtle object you want to move
        step (int)- the amount of displacement at each timestep (speed)
        anglerange (int) - the range of angle headings the turtle can take. enter 0-180."""
    # random walks require a random direction and even step size
    # levy walks require random direction and variable step sizes (play around!)
    angle = random.randint(-anglerange, anglerange) # choose a random direction
    turt.setheading(angle) # face the turtle to that random angle
    turt.forward(step)

# set up the turtle
rw.shapesize(0.5)
rw.color('darkblue')
rw.up() # don't draw, just move

while running:
    

    
    counter += 1
    
    # animation stop condition
    if counter > 1000:
        running = False
    
    time.sleep(.03)
    turtle.update() # draw the updated image on the screen.
        
turtle.done() # clean up
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
This code is NOT in function form, but probably should be.........cough cough.
"""

import turtle 
import time, random # to control framrate and add randomness
turtle.colormode(255)
turtle.tracer(0) #turn off animation

running = True # control the animation loop
counter = 0 # "timer" to stop the code

step = 5 # speed of random walk
anglerange = 180 # angular distribution
# make ^ number smaller to have a more pointed direction
rw = turtle.Turtle(shape='circle') # random walk

# set up the turtle
rw.shapesize(0.5)
rw.color('darkblue')
rw.up() # don't draw, just move

while running:
    
    # random walks require a random direction and even step size
    # levy walks require random direction and variable step sizes (play around!)
    angle = random.randint(-anglerange, anglerange) # choose a random direction
    rw.setheading(angle) # face the turtle to that random angle
    rw.forward(step)
    
    counter += 1
    
    # animation stop condition
    if counter > 1000:
        running = False
    
    time.sleep(.03)
    turtle.update() # draw the updated image on the screen.
        
turtle.done() # clean up
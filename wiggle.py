#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:23:14 2021

@author: sazamore
Wiggle animation
Taken from FA2020 Bubble code

This code demonstrates how to animate a wiggling turtle.
This movement can be used in combination with other movements.
This code is NOT in function form, but probably should be.........cough cough.
"""

import turtle 
import time # to control framrate and add randomness
turtle.colormode(255)
turtle.tracer(0) #turn off animation

running = True # control the animation loop
counter = 0 # "timer" to stop the code

step = 2 # the amound of displacement the circle will wiggle
wiggle = turtle.Turtle(shape='circle')

# set up the turtle
wiggle.shapesize(3)
wiggle.color('maroon','cornsilk')
wiggle.up() # don't draw, just move

while running:
    wiggle.forward(step)
    step *= -1 # change the value to the opposite sign to move in the opposite direction
    
    counter += 1
    
    # animation stop condition
    if counter > 100:
        running = False
    
    time.sleep(.03)
    turtle.update() # draw the updated image on the screen.
        
turtle.done() # clean up
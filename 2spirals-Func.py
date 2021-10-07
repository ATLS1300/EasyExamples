#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:23:14 2021

@author: sazamore
Spiral movement animation

This code demonstrates how to animate a spiraling movement using 2 turtles.
This movement can be used in combination with other movements.
This code is in function-based form.
"""

import turtle 
import time, random # to control framrate and add randomness
turtle.colormode(255)
turtle.tracer(0) #turn off animation

running = True # control the animation loop
side = 5 # size of spiral

# define & setup turtles
spiralLeft = turtle.Turtle() 
spiralLeft.shapesize(2)
spiralLeft.color('orange')
spiralLeft.width(10) # drawing and movement

spiralRight = spiralLeft.clone() # make an identical turtle with the same settings
spiralRight.color('orangered4')
spiralLeft.setheading(180) # face the left

# define functions
def spiral(turt, side=5, angle=105, inc=1):
    """Sends a turtle along an outward spiraling path.
    Code modified from https://holypython.com/turtle-spirals/
    Arguments:
        turt (turtle) - a turtle object you wish to move
        (optional) step (int)- the step of each 'side' of the spiral
        (optional) inc (int)- determines the density of the spiral (larger numbers are LESS dense)
        (optional) angle (int)- determines the density (larger numbers are MORE dense)"""
    turt.forward(side)
    turt.right(15)
    side += inc
    return side

while running:
    
    spiral(spiralLeft,side)
    side = spiral(spiralRight,side)    
    
    # animation stop condition
    if side > 200:
        running = False
    
    time.sleep(.03) # sets speed of animation. Larger numbers are slower
    turtle.update() # draw the updated image on the screen.
        
turtle.done() # clean up
# Author: github.com/mcswe
# Date: 12 February 2020

import turtle
import random

def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle for coloring pixels. Return a turtle
        object in hidden state with its pen up. The canvas has size canv_width
        by canv_height, with a coordinate system where (0,0) is in the bottom
        left corner, and automatic re-drawing of the canvas is disabled so that
        turtle.update() must be called to update the drawing.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()

    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255

    t.up() # lift the pen
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement

    return t

def coordinate(): #see spec below
    '''
    Chooses one of the corners of the triangle by random.
    Preconditions: canvas width and height are already defined
    Postconditions: none
    '''
    return random.choice([(0.5*canv_width, canv_height),(0,0), (canv_width,0)])
    
def midpoint(a, b):
    """ Return the midpoint between points a = (ax, ay) and b = (bx, by) """
    ax, ay = a
    bx, by = b
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    return mx, my

def pyth_theorem(a, b): #this finds the distance between any two points
    ax, ay = a
    bx, by = b
    
    return (((bx - ax)**2 + (by-ay)**2)**0.5)

def choose_color(m): #this function chooses the color of the pixel based off its distance from each corner
    
    corner1 = (0.5*(canv_width), canv_height) #red
    corner2 = (0,0) #green
    corner3 = (canv_width, 0) #blue
    
    #max_distance is the largest possible distance between two points within the triangle
    max_distance = max([pyth_theorem(corner1, corner2)  , pyth_theorem(corner2, corner3)]) 
    
    #we subtract (the distance from the point to the corner into a color value) from 255.
    #so the larger the distance, the less of the color there will be.
    red = int(255-((pyth_theorem(m, corner1))*255)/max_distance)
    green = int(255-((pyth_theorem(m, corner2))*255)/max_distance)
    blue = int(255-((pyth_theorem(m, corner3))*255)/max_distance)
    
    return (red,green,blue)


if __name__ == "__main__":    
    import sys
    import turtle
    
    # width and height are given as command line arguments:
    canv_width = int(sys.argv[1])
    canv_height = int(sys.argv[2])
    
    t = turtle_setup(500, 500)
    # Write your main program here.
    
    # Start by calling the turtle_setup function.
    turtle_setup(canv_width, canv_height)
    # Then implement the pseudocode below:
    
    # Chaos game - pseudocode from the assignment handout:
    # Let p be a random point in the window
    p = (random.randint(0, canv_width), random.randint(0, canv_height))
    
    # loop 10000 times:
    for i in range(10000):
    #     c = a random corner of the triangle
        c = coordinate()
    #     m = the midpoint between p and c
        m = midpoint(p,c)
        t.penup()
        t.goto(m)
        t.pendown()
    #     choose a color for m with choose_color function
        t.color(choose_color(m))
    #     color the pixel at m
        if i > 10:
            t.dot(4)
    #     p=m
        p = m

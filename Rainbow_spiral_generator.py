from turtle import *
from colorsys import hsv_to_rgb
colormode(1.0)
penup()
setposition(0,0)
pendown()
speed(0)
bgcolor('black')
pensize(3)

h=0  # Initial hue value (0 to 1)

# The outer loop determines the number of 'rotations' or distinct color sets
for j in range(120):
    # The inner loop draws one part of the pattern (a 'square-like' shape)
    for i in range(4):
        # Set the color using the current hue (h)
        # S=1 (saturation) and V=1 (value/brightness) for vivid colors
        color(hsv_to_rgb(h, 1, 1))

        # This is the way to increment the hue:
        h += 0.003 # Increment hue for the next segment

        # The pattern drawing logic
        circle(40 + i * 5, 90)
        forward(250)
        left(90)

    # Rotate the entire drawing context for the next outer loop iteration
    rt(10)

hideturtle()
done()
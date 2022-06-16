import turtle

import pygame
import numpy
import random
import math

screen = turtle.Screen()
screen.title('Snake')
screen.setup(width=900, height=900)
screen.tracer(0)
turtle.bgcolor('turquoise')

turtle.speed(4)
turtle.pensize(2)
turtle.goto(-310, 250)

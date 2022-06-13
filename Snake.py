import pygame
import numpy
import random
import math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
grid = numpy.zeros((20, 20), dtype="int8")
for i in range(4):
    grid[7][2+i] = 2

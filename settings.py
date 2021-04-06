#!/usr/bin/python
"""
File with all settings and gameplay varaibles
"""
import pygame

# window size
_WIDTH = 600
_HEIGHT = 780
# player stats
_PlayerSPEED = 2
# load sprites
bgImage = pygame.image.load("sprites/background.png")
heartImage = pygame.image.load("sprites/heart.png")
carsImgs = [
    pygame.image.load("sprites/car1.png"),
    pygame.image.load("sprites/car2.png"),
    pygame.image.load("sprites/car3.png"),
]
turtleImages = [pygame.image.load("sprites/turtle1.png"),
                pygame.image.load("sprites/turtle2.png"),
                pygame.image.load("sprites/turtle1.png"),
                pygame.image.load("sprites/turtle3.png")]

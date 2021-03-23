#!/usr/bin/python
"""
a file with game class
"""
import settings
import pygame
import sys

class Game:
    
    #init method called when game starts
    def __init__(self):
        self.gameON = True
        self.screen = pygame.display.set_mode((settings._WIDTH, settings._HEIGHT))
    
    def play(self):
        while self.gameON:
            self.manageInput()
            pygame.display.update()

    def manageInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
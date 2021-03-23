#!/usr/bin/python
"""
a file with game class
"""
import settings,player
import pygame
import sys

class Game:
    
    #init method
    def __init__(self):
        self.gameON = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((settings._WIDTH, settings._HEIGHT))
        self.newGame()
    
    #main loop of the game
    def play(self):
        while self.gameON:
            #draw elements
            self.drawElements()
            #show elements
            pygame.display.update()

            self.manageInput()
            
            self.clock.tick(60)

    #method to manage player input
    def manageInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def drawElements(self):
        self.screen.fill((255,255,255))
        self.P1.blit()
        

    #make new game
    def newGame(self):
        self.P1 = player.Player(self.screen)
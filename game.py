#!/usr/bin/python
"""
a file with game class
"""
import settings,player,car
import pygame
from pygame.locals import *
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
            #update elements
            self.update()

            #draw elements
            self.drawElements()

            #show elements
            pygame.display.update()

            #manage player input
            self.manageInput()
            
            #static 60 fps framerate
            self.clock.tick(60)

    #method to manage player input
    def manageInput(self):
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.P1.goUp()
                elif  event.key == K_s:
                    self.P1.goDown()

            elif  event.type == KEYUP:
                if event.key == K_w:
                    self.P1.stay()
                elif  event.key == K_s:
                    self.P1.stay()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            
    #one methon with all drawnings
    def drawElements(self):
        self.screen.blit(settings.bgImage,(0,0))
        self.P1.blit()
        self.Cars.draw(self.screen)
    
    #method to update elements
    def update(self):
        self.Cars.update()
        self.P1.update()
        
    #make new game
    def newGame(self):
        self.P1 = player.Player(self.screen)
        self.generateCars()
    
    #generate cars
    def generateCars(self):
        self.Cars = pygame.sprite.Group()
        self.Cars.add(car.Car(60))
        self.Cars.add(car.Car(140))
        self.Cars.add(car.Car(280))
        self.Cars.add(car.Car(360))
        self.Cars.add(car.Car(500))
        self.Cars.add(car.Car(580))
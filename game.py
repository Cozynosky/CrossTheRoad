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
        pygame.init()
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

    #create new game
    def newGame(self):
        self.level = 1
        self.P1 = player.Player(self.screen)
        self.prepareLevel()
    #method to manage player input
    def manageInput(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.P1.forward = True
                if  event.key == K_s:
                    self.P1.backward = True
                if event.key == K_a:
                    self.P1.left = True
                if event.key == K_d:
                    self.P1.right = True

            elif  event.type == KEYUP:
                if event.key == K_w:
                    self.P1.forward = False
                if  event.key == K_s:
                    self.P1.backward = False
                if event.key == K_a:
                    self.P1.left = False
                if event.key == K_d:
                    self.P1.right = False

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            
    #one methon with all drawnings
    def drawElements(self):
        self.screen.blit(settings.bgImage,(0,0))
        self.P1.blit()
        self.Cars.draw(self.screen)
        self.screen.blit(self.levelText,self.level_rect)
        self.screen.blit(self.hearts, self.hearts_rect)
    
    #prepare level text
    def prepareLevelText(self):
        #prepare font for level showing
        levelFont = pygame.font.SysFont("Tw Cen MT Condensed Extra Bold,", 51)
        self.levelText = levelFont.render("Level: "+ str(self.level), True, (0,0,0))
        self.level_rect = self.levelText.get_rect()
        self.level_rect.center = (settings._WIDTH//2,30)

    #prepare players lifes to show on screen
    def prepareHearts(self):
        self.hearts = pygame.Surface((90,30),pygame.SRCALPHA)
        for i in range(self.P1.lifes):
            self.hearts.blit(settings.heartImage,(i*30,0))
        self.hearts_rect = self.hearts.get_rect()
        self.hearts_rect = (30,15)

    #method to update elements
    def update(self):
        self.checkCrash()
        self.checkLevelComplete()
        self.P1.update()
        self.Cars.update()
        
    #check if player has crashed with a car
    def checkCrash(self):
        if pygame.sprite.spritecollideany(self.P1,self.Cars):
            if self.P1.lifes == 1:
                self.gameON = False
            else:
                self.P1.lifes -= 1
                self.P1.resetPos()
                self.prepareHearts()

    #check if level is done
    def checkLevelComplete(self):
        if self.P1.rect.bottom < 120:
            self.level += 1
            self.prepareLevelText()
            self.P1.resetPos()
            self.prepareLevel()

    #prepare new level
    def prepareLevel(self):
        self.generateCars()
        self.prepareLevelText()
        self.prepareHearts()

    #prepare GameOver method
    def gameOver(self):
        gameOverFont = pygame.font.SysFont("Tw Cen MT Condensed Extra Bold,", 100)
        gameOverText = gameOverFont.render("GAME OVER", True, (0,0,0))
        gameOver_rect = gameOverText.get_rect()
        gameOver_rect.center = (settings._WIDTH//2,settings._HEIGHT//2)
        self.screen.blit(gameOverText,gameOver_rect)

    #generate cars
    def generateCars(self):
        self.Cars = pygame.sprite.Group()
        self.Cars.add(car.Car(120,self.level))
        self.Cars.add(car.Car(200,self.level))
        self.Cars.add(car.Car(340,self.level))
        self.Cars.add(car.Car(420,self.level))
        self.Cars.add(car.Car(560,self.level))
        self.Cars.add(car.Car(640,self.level))
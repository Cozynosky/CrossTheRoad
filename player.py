#!/usr/bin/python
"""
file with player class
"""
import pygame
import settings

class Player:

    #init method
    def __init__(self,screen):
        self.newPlayer()
        self.screen = screen
    
    #method to create new player when game starts
    def newPlayer(self):
        #player starts with 0 points
        self.score = 0
        #temp player without graphics
        self.image = pygame.Surface((40,40))
        self.image.fill((255,0,0))
        #make rect from image and set corret position
        self.rect = self.image.get_rect()
        self.rect.centerx = settings._WIDTH//2
        self.rect.bottom = settings._HEIGHT - 20
        #player stays when movement is 0, go up when <0 or go down when >0
        self.movement = 0

    #reacton on player up input
    def goUp(self):
        if self.movement == 0:
            self.movement = -settings._PlayerSPEED

    #reacton on player down input
    def goDown(self):
        if self.movement == 0:
            self.movement = settings._PlayerSPEED

    #reaction when player wants to stop moving        
    def stay(self):
        if self.movement != 0:
            self.movement = 0

    #update player position
    def update(self):
        #update position only when player wont hit bottom
        if self.rect.bottom+self.movement <= settings._HEIGHT:
            self.rect.y += self.movement
    
    #method to blit player on screen
    def blit(self):
        self.screen.blit(self.image,self.rect)


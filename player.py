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
    
    def newPlayer(self):
        #player starts with 0 points
        self.score = 0
        self.image = pygame.Surface((40,40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = settings._WIDTH//2
        self.rect.bottom = settings._HEIGHT - 20
    
    def blit(self):
        self.screen.blit(self.image,self.rect)


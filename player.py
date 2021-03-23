#!/usr/bin/python
"""
file with player class
"""
import pygame
import settings

class Player(pygame.sprite.Sprite):

    #init method
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        #player starts with 3 lifes
        self.lifes = 3
        #temp player without graphics
        self.image = pygame.Surface((40,40))
        self.image.fill((255,0,0))
        #set player position
        self.resetPos()
    
    #method to create new player when game starts
    def resetPos(self):
        #make rect from image and set corret position
        self.rect = self.image.get_rect()
        self.rect.centerx = settings._WIDTH//2
        self.rect.bottom = settings._HEIGHT - 20
        #player can go forward, backward, left or right
        self.forward = False
        self.backward = False
        self.left = False
        self.right = False

    #update player position
    def update(self):
        #update position only when player wont hit bottom
        if self.forward and self.rect.top > 60:
            self.rect.y -= settings._PlayerSPEED
        if self.backward and self.rect.bottom < settings._HEIGHT:
            self.rect.y += settings._PlayerSPEED
        if self.right and self.rect.right < settings._WIDTH:
            self.rect.x += settings._PlayerSPEED
        if self.left and self.rect.left > 0:
            self.rect.x -= settings._PlayerSPEED
    
    #method to blit player on screen
    def blit(self):
        self.screen.blit(self.image,self.rect)


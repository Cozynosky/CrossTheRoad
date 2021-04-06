#!/usr/bin/python
"""
file with player class
"""
import pygame
import settings


class Player(pygame.sprite.Sprite):

    # init method
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        # player starts with 3 lifes
        self.lifes = 3
        # set player position
        self.resetPos()

    # method to create new player when game starts
    def resetPos(self):
        #load image
        self.image = settings.turtleImage
        # make rect from image and set corret position
        self.rect = self.image.get_rect()
        self.rect.centerx = settings._WIDTH // 2
        self.rect.bottom = settings._HEIGHT - 20
        # player can go forward, backward, left or right
        self.forward = False
        self.backward = False
        self.left = False
        self.right = False
        
    # update player position
    def update(self):
        # update position only when player wont hit bottom
        if self.forward and self.rect.top > 60:
            self.rect.y -= settings._PlayerSPEED
        if self.backward and self.rect.bottom < settings._HEIGHT:
            self.rect.y += settings._PlayerSPEED
        if self.right and self.rect.right < settings._WIDTH:
            self.rect.x += settings._PlayerSPEED
        if self.left and self.rect.left > 0:
            self.rect.x -= settings._PlayerSPEED
        #load image
        self.loadImage()

    # method to blit player on screen
    def blit(self):
        self.screen.blit(self.image, self.rect)

    #method to load image
    def loadImage(self):
        #change image only if player dont push 
        if not ((self.forward and self.backward) or (self.left and self.right)):
            if self.forward:
                self.image = settings.turtleImage
                #if player wants to go daigonally -> rotate image
                if self.left:
                    self.image = pygame.transform.rotate(self.image,15)
                if self.right:
                    self.image = pygame.transform.rotate(self.image,-15)    
            elif self.backward:
                self.image = pygame.transform.flip(settings.turtleImage,False,True)
                #if player wants to go daigonally -> rotate image
                if self.left:
                    self.image = pygame.transform.rotate(self.image,-15)
                if self.right:
                    self.image = pygame.transform.rotate(self.image,15)
            elif self.left:
                self.image = pygame.transform.rotate(settings.turtleImage,90)
            elif self.right:
                self.image = pygame.transform.rotate(settings.turtleImage,-90)
            #rotating image changes the rect of image
            oldCenter = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter
            
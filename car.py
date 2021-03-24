#!/usr/bin/python
"""
file with Car class
"""
import pygame
import random
import settings

class Car(pygame.sprite.Sprite):

    #init method
    def __init__(self,yPos,level):
        self.level = level
        pygame.sprite.Sprite.__init__(self)
        self.newCar(yPos)

    #method to create new car
    def newCar(self,yPos):
        #car can go left or right
        self.facing = random.choice(["Right","Left"])
        #load car image depends on facing
        self.loadImage()
        self.rect = self.image.get_rect()
        self.rect.y = yPos
        #reset car position when make new one
        self.resetCar()

    #reset car, when hit wall for example
    def resetCar(self):
        if self.facing == "Left":
            self.rect.left = settings._WIDTH
        else:
            self.rect.right = 0; 
        #radomize car speed
        self.prepareSpeed()
        #load new random img
        self.loadImage()
    
    #load car image mathod
    def loadImage(self):
        self.image = random.choice(settings.carsImgs)
        if self.facing == "Left":
           self.image = pygame.transform.flip(self.image, True, False)

    #prepare car speed basing on level
    def prepareSpeed(self):
        if self.level < 6:
            self.speed = random.randint(self.level,self.level+3)
        else:
            self.speed = random.randint(6,9)
    
    #update car pos
    def update(self):
        if self.facing == "Right":
            if self.rect.left >= settings._WIDTH:
                self.resetCar()
            else:
                self.rect.x += self.speed
        else:
            if self.rect.right <= 0:
                self.resetCar()
            else:
                self.rect.x -= self.speed
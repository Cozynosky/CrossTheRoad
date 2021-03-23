#!/usr/bin/python
"""
file with Car class
"""
import pygame
import random
import settings

class Car(pygame.sprite.Sprite):

    #init method
    def __init__(self,yPos):
        pygame.sprite.Sprite.__init__(self)
        self.newCar(yPos)

    #method to create new car
    def newCar(self,yPos):
        #temp car without graphics
        self.image = pygame.Surface((80,60))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.y = yPos
        #car can go left or right
        self.facing = random.choice(["Right","Left"])
        #reset car position when make new one
        self.resetCar()
    
    #reset car, when hit wall for example
    def resetCar(self):
        if self.facing == "Left":
            self.rect.left = settings._WIDTH
        else:
            self.rect.right = 0; 
        #radomize car speed
        self.speed = random.choice([3,4,5,6])
    
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
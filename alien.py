import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Class represnets a single alien object
    def __init__(self, siGame):
        super().__init__()
        self.screen = siGame.screen
        self.settings = siGame.settings

        #Loading alien image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #Start alien on the top left of game screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store alien horizontal position
        self.x = float(self.rect.x)
    
    def checkEdges(self):
        # Return True if there is an alien at the edge of game screen
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right or self.rect.left <= 0:
            return True

    def update(self):
        #Move aliens right
        self.x += self.settings.alienSpeed
        self.rect.x =self.x

import pygame

class Ship:
    # SpaceShip management and features
    def __init__(self, aiGame):
        self.screen = aiGame.screen
        self.screenRect = aiGame.screen.get_rect()

        #Loading image and get rectangle of image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Positioning ship at the bottom center of screen
        self.rect.midbottom = self.screenRect.midbottom
    
    def blitme(self):
        # Draw ship
        self.screen.blit(self.image, self.rect)
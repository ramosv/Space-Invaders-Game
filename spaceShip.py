import pygame
#from settings import Settings

class Ship:
    # SpaceShip management and features
    def __init__(self, siGame):
        self.screen = siGame.screen
        self.screenRect = siGame.screen.get_rect()
        self.settings = siGame.settings

        #Loading image and get rectangle of image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        #self.bgColor = self.Settings.bgcolor()

        #Positioning ship at the bottom center of screen
        self.rect.midbottom = self.screenRect.midbottom

        #Value for speed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        #Movement
        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False

    def update(self):
        #update ship position
        if self.moveRight:
            self.x += self.settings.shipSpeed
        if self.moveLeft:
            self.x -= self.settings.shipSpeed
        if self.moveUp:
            self.y += self.settings.shipSpeed
        if self.moveDown:
            self.y -= self.settings.shipSpeed

        #update rectable objext from self.x (update the value and send it back)
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        # Draw ship
        self.screen.blit(self.image, self.rect)
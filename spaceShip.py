import pygame
from pygame.sprite import Sprite

# from settings import Settings


class Ship(Sprite):
    # SpaceShip management and features
    def __init__(self, siGame):
        super().__init__()
        self.screen = siGame.screen
        self.screenRect = siGame.screen.get_rect()
        self.settings = siGame.settings

        # Loading image and get rectangle of image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # self.bgColor = self.Settings.bgcolor()

        # Positioning ship at the bottom center of screen
        self.rect.midbottom = self.screenRect.midbottom

        # Value for speed
        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

        # Movement
        self.moveRight = False
        self.moveLeft = False
        # self.moveUp = False
        # self.moveDown = False

    def update(self):
        # update ship position and keep it inbounds of screen
        if self.moveRight and self.rect.right < self.screenRect.right:
            self.x += self.settings.shipSpeed
        if self.moveLeft and self.rect.left > 0:
            self.x -= self.settings.shipSpeed
        # if self.moveUp and self.rect.top > 0 :
        #     self.y -= self.settings.shipSpeed
        # if self.moveDown and self.rect.bottom < self.screenRect.top:
        #     self.y += self.settings.shipSpeed

        # update rectable objext from self.x (update the value and send it back)
        self.rect.x = self.x
        # self.rect.y = self.y

    def blitme(self):
        # Draw ship
        self.screen.blit(self.image, self.rect)

    def centerShip(self):
        self.rect.midbottom = self.screenRect.midbottom
        self.x = float(self.rect.x)

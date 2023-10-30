import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    ##Bullets fired from ship

    def __init__(self, siGame):
        ##Super since we building on top of Sprite
        super().__init__()
        self.screen = siGame.screen
        self.settings = siGame.settings
        self.color = self.settings.bulletColor

        # Create a bullet rectable at (0,0) and then set correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.bulletWidth, self.settings.bulletHeight
        )
        self.rect.midtop = siGame.ship.rect.midtop

        # Store bullets position as float
        self.y = float(self.rect.y)

    def update(self):
        # Move bullets through y axis
        self.y -= self.settings.bulletSpeed
        # Update position of rectangle
        self.rect.y = self.y

    def drawBullet(self):
        # Drawing the bullet
        pygame.draw.rect(self.screen, self.color, self.rect)

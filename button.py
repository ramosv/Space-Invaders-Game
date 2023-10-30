import pygame.font


class Button:
    def __init__(self, siGame, msg):
        self.screen = siGame.screen
        self.screenRect = self.screen.get_rect()

        # dimensions and properties of button
        self.width, self.height = 200, 100
        self.buttonColor = (0, 0, 0)
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center

        # Prep msg
        self._prepMsg(msg)

    def _prepMsg(self, msg):
        self.msgImage = self.font.render(msg, True, self.textColor, self.buttonColor)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.rect.center

    def drawButton(self):
        # blank button then draw message
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage, self.msgImageRect)

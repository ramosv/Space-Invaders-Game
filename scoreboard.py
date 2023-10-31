import pygame.font
from pygame.sprite import Group

from spaceShip import Ship


class ScoreBoard:
    def __init__(self, siGame):
        "Score keeping attributes"
        self.siGame = siGame
        self.screen = siGame.screen
        self.screenRect = siGame.screen.get_rect()
        self.settings = siGame.settings
        self.stats = siGame.stats

        # Font for scoring info
        self.textColor = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prepScore()
        self.prepHighScore()
        self.prepLevel()
        self.prepShips()

    def prepScore(self):
        # Turn score into rendered image
        roundScore = round(self.stats.score, -1)
        scoreStr = "Score: {:,}".format(roundScore)
        self.scoreImage = self.font.render(
            scoreStr, True, self.textColor, self.settings.bgColor
        )

        # Display score on top right of screen
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20

    def prepHighScore(self):
        # Turn score into rendered image
        roundScore = round(self.stats.score, -1)
        highScore = "HighScore: {:,}".format(roundScore)
        self.highScoreImage = self.font.render(
            highScore, True, self.textColor, self.settings.bgColor
        )

        # Display high score in the center of screen
        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = 20

    def prepLevel(self):
        levelStr = str(f"Level: {self.stats.level}")
        self.levelImage = self.font.render(
            levelStr, True, self.textColor, self.settings.bgColor
        )

        # Position level below score
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.scoreRect.right
        self.levelRect.top = self.scoreRect.bottom + 10

    def prepShips(self):
        # Show ships as lives
        self.ships = Group()
        for shipNumber in range(self.stats.shipsLeft):
            ship = Ship(self.siGame)
            ship.rect.x = 10 + shipNumber * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def showScore(self):
        # draw score
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.screen.blit(self.levelImage, self.levelRect)
        self.ships.draw(self.screen)

    def checkHighScore(self):
        # Check if new score is higher
        if self.stats.score > self.stats.highScore:
            self.stats.highScore = self.stats.score
            self.prepHighScore()

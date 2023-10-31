import sys
import pygame
from time import sleep

from settings import Settings
from spaceShip import Ship
from bullet import Bullet
from alien import Alien
from gameStats import GameStats
from button import Button
from scoreboard import ScoreBoard


# Main class that manages the game
class spaceInvader:
    def __init__(self):
        # start the game
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screenWidth = self.screen.get_rect().width
        self.settings.screenHeight = self.screen.get_rect().height

        pygame.display.set_caption("Space Invader")

        # Create an instace to store game statistics
        self.stats = GameStats(self)
        self.scoreBoard = ScoreBoard(self)

        # Highscore is never reset

        self.ship = Ship(self)
        # instanciate bullets you can think of sprite.group() as an array of bullet objects
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        # Creating the fleet of aliens
        self._createFleet()

        # Instance of play button
        self.playButton = Button(self, "Start Game")

        # Background color
        self.bgColor = self.settings.bgColor

    def runGame(self):
        # Main loop for the game
        while True:
            # Keybord and mouse events
            self._checkEvents()

            # As long as ship has lives left
            if self.stats.gameActive:
                self.ship.update()
                self._updateBullets()
                self._updateAliens()

            self._updateScreen()

    def _checkEvents(self):
        # Responds to mouse and keyboard events
        for event in pygame.event.get():
            # Executed when we close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Key presses
                self._checkKeyDownEvents(event)
            elif event.type == pygame.KEYUP:
                # Key release
                self._checkKeyUpEvents(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                self._checkPlayButton(mousePos)

    def _checkPlayButton(self, mousePos):
        # Start game when player click button
        buttonClicked = self.playButton.rect.collidepoint(mousePos)
        if buttonClicked and not self.stats.gameActive:
            ##Reset game settings and stats
            self.settings.dynamicSettings()
            self.stats.resetStats()
            self.stats.gameActive = True
            self.scoreBoard.prepScore()
            self.scoreBoard.prepLevel()
            self.scoreBoard.prepShips()

            # Clear screen (aliens and bullets)
            self.aliens.empty()
            self.bullets.empty()

            # Create a fresh fleet
            self._createFleet()
            self.ship.centerShip()

            # Hide mouse
            pygame.mouse.set_visible(False)

    def _checkKeyDownEvents(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moveRight = True
        elif event.key == pygame.K_LEFT:
            self.ship.moveLeft = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fireBullet()

        # elif event.key == pygame.K_UP:
        #         self.ship.moveUp = True
        # elif event.key == pygame.K_DOWN:
        #         self.ship.moveDown = True

    def _checkKeyUpEvents(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moveRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.moveLeft = False
        # elif event.key == pygame.K_UP:
        #     self.ship.moveUp = False
        # elif event.key == pygame.K_DOWN:
        #     self.ship.moveDown = False

    def _fireBullet(self):
        # Limiting the amount of bullets in screen at once
        if len(self.bullets) < self.settings.bulletLimit:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)

    def _updateBullets(self):
        self.bullets.update()

        # Deleting bullets when they reach top
        # Creating a copy as you cannot change the size of strucuure as you iterate throigh it
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # Checking if bullets are actually deleted
            # print(len(self.bullets))

        self.checkAlienBulletCollision()

        if not self.aliens:
            # New fleet if current is destryed
            self.bullets.empty()
            self._createFleet()

    def checkAlienBulletCollision(self):
        # Collion detection return a dict with items from two different sprite groups that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                # awarding points for each alien that is hit
                self.stats.score += self.settings.alienPoints * len(aliens)
            self.scoreBoard.prepScore()
            self.scoreBoard.checkHighScore()

        if not self.aliens:
            # New fleet if current is destryed
            self.bullets.empty()
            self._createFleet()
            self.settings.increaseSpeed()

            # Increase level
            self.stats.level += 1
            self.scoreBoard.prepLevel()

    def _updateAliens(self):
        self._checkFleetEdges()
        self.aliens.update()

        # Check for ship and alien collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._shipHit()

        # Check for aliens hittin bottom of screen
        self._checkAliensBottom()

    def _shipHit(self):
        # decrement ships
        if self.stats.shipsLeft > 0:
            self.stats.shipsLeft -= 1
            self.scoreBoard.prepShips()

            # Clear the screen
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and ship
            self._createFleet()
            self.ship.centerShip()

            # pause
            sleep(0.5)
        else:
            self.stats.gameActive = False
            pygame.mouse.set_visible(True)

    def _checkAliensBottom(self):
        screenRect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screenRect.bottom:
                # Same as if the ship got hit
                self._shipHit()
                break

    def _createFleet(self):
        # make an alien fleet to fill up screen
        # The space between the aliens will equal to another alien
        alien = Alien(self)
        alienWidth, alienHeight = alien.rect.size
        totalSpaceX = self.settings.screenWidth - (2 * alienWidth)
        totalAliens = totalSpaceX // (2 * alienWidth)

        # Determine max number of rows of aliens that fit on screen
        shipHeight = self.ship.rect.height
        availSpcaceY = self.settings.screenHeight - (3 * alienHeight) - shipHeight
        numberRows = availSpcaceY // (2 * alienHeight)

        # Rows of aliens fleet
        for rowNum in range(numberRows):
            # Create aliena and place in the row
            for alienNum in range(totalAliens):
                self._createAlien(alienNum, rowNum)

    def _createAlien(self, alienNumber, rowNumber):
        alien = Alien(self)
        alienWidth, alienHeight = alien.rect.size
        alien.x = alienWidth + 2 * alienWidth * alienNumber
        alien.rect.x = alien.x
        alien.rect.y = alienHeight + 2 * alien.rect.height * rowNumber
        self.aliens.add(alien)

    def _checkFleetEdges(self):
        # Checking if an alien reached edge
        for alien in self.aliens.sprites():
            if alien.checkEdges():
                self._changeFleetDirection()
                break

    def _changeFleetDirection(self):
        # Drop fleet down
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleetDropSpeed
        self.settings.fleetDirection *= -1

    def _updateScreen(self):
        # Fills background color after each iteration
        self.screen.fill(self.settings.bgColor)
        self.ship.blitme()
        # Bullets group is kind of an array so we are iterating through each bullet we create and updating it
        for bullet in self.bullets.sprites():
            bullet.drawBullet()
        self.aliens.draw(self.screen)

        # Draw score info
        self.scoreBoard.showScore()

        # Draw the play button if the game is inactive
        if not self.stats.gameActive:
            self.playButton.drawButton()

        # Update the screen with new elements and updates
        pygame.display.flip()


if __name__ == "__main__":
    # Making a game instance to run the game
    game = spaceInvader()
    game.runGame()

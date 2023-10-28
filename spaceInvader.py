import sys
import pygame
from settings import Settings
from spaceShip import Ship
from bullet import Bullet
from alien import Alien

#Main class that manages the game
class spaceInvader:
    def __init__(self):
        #start the game 
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screenWidth = self.screen.get_rect().width
        self.settings.screenHeight = self.screen.get_rect().height
        
        pygame.display.set_caption("Space Invader")

        self.ship = Ship(self)
        #instanciate bullets you can think of sprite.group() as an array of bullet objects
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        #Creating the fleet of aliens
        self._createFleet()

        #Background color
        self.bgColor = self.settings.bgColor

    def runGame(self):
        #Main loop for the game
        while True:
            #Keybord and mouse events
            self._checkEvents()
            self.ship.update()  
            self._updateBullets()
            self._updateAliens()
            self._updateScreen()   
        
    def _checkEvents(self):
        #Responds to mouse and keyboard events
        for event in pygame.event.get():
            #Executed when we close the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    #Key presses
                    self._checkKeyDownEvents(event)
            elif event.type == pygame.KEYUP:
                    #Key release
                    self._checkKeyUpEvents(event)
    
    def _checkKeyDownEvents(self,event):
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
    
    def _checkKeyUpEvents(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moveRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.moveLeft = False
        # elif event.key == pygame.K_UP:
        #     self.ship.moveUp = False
        # elif event.key == pygame.K_DOWN:
        #     self.ship.moveDown = False
    
    def _fireBullet(self):
         #Limiting the amount of bullets in screen at once
         if len(self.bullets) < self.settings.bulletLimit:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)
    
    def _updateBullets(self):
        self.bullets.update()

        #Deleting bullets when they reach top
        #Creating a copy as you cannot change the size of strucuure as you iterate throigh it
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                #Checking if bullets are actually deleted
                #print(len(self.bullets))
    def _updateAliens(self):
         self.aliens.update()
    
    def _createFleet(self):
         #make an alien fleet to fill up screen
         #The space between the aliens will equal to another alien
         alien = Alien(self)
         alienWidth, alienHeight = alien.rect.size
         totalSpaceX = self.settings.screenWidth - (2 * alienWidth)
         totalAliens = totalSpaceX // (2* alienWidth)

         #Determine max number of rows of aliens that fit on screen
         shipHeight = self.ship.rect.height
         availSpcaceY = (self.settings.screenHeight - (3*alienHeight) - shipHeight)
         numberRows = availSpcaceY // (2*alienHeight)

         #Rows of aliens fleet
         for rowNum in range(numberRows):
                #Create aliena and place in the row
                for alienNum in range(totalAliens):
                     self._createAlien(alienNum, rowNum)
    
    def _createAlien(self,alienNumber,rowNumber):
         alien = Alien(self)
         alienWidth, alienHeight = alien.rect.size
         alien.x = alienWidth + 2 * alienWidth * alienNumber
         alien.rect.x = alien.x
         alien.rect.y = alienHeight + 2 * alien.rect.height * rowNumber
         self.aliens.add(alien)
                    

    def _updateScreen(self):
         #Fills background color after each iteration
            self.screen.fill(self.settings.bgColor)
            self.ship.blitme()
            #Bullets group is kind of an array so we are iterating through each bullet we create and updating it
            for bullet in self.bullets.sprites():
                 bullet.drawBullet()
            self.aliens.draw(self.screen)

            #Update the screen with new elements and updates
            pygame.display.flip()
         

if __name__ == "__main__":
    #Making a game instance to run the game
    game = spaceInvader()
    game.runGame()
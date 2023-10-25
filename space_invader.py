import sys
import pygame


#Main class that manages the game
class spaceInvader:
    def __init__(self) -> None:
        #start the game 
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Space Invader")

        #Background color
        self.bg_color = (208,193,193)

    def run_game(self):
        #Main loop for the game
        while True:
            #Keybord and mouse events
            for event in pygame.event.get():
                #Executed when we close the game
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Fills background color after each eteration
            self.screen.fill(self.bg_color)

            #Update the screen with new elements and updates
            pygame.display.flip()

if __name__ == "__main__":
    #Making a game instance to run the game
    game = spaceInvader()
    game.run_game()
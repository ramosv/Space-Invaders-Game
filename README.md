# Space-Invaders-game
Space Invaders style video game built using Pygame
This game was built with assitance from the book Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming 2nd Edition
At the start of chapter 12, we start building this Space Invader Style game using Pygame python library


Project plan
Player will control a rocket shit that moves left to right with the capability of shooting
Implement a Object Oriented Programming design by having all interacting objects be a python class
In summary this will be the file structure
 - alien.py
    - Each alien object will represent a single alien on the screen. In the main file we will be creating a fleet of these alien objects.
 - bullet.py
    - Representing the bullets that originate from te spaceShip aimed at the aliens. Alien, bullets and spaceShip will incorpocate collision detection.
 - button.py
    - Start button for the game
 - gameStats.py
    - keeping track of current score and high schore
 - scoreBoard.py
    - Dislaying score from gameStats, level and lives left.
 - settings.py
    - Game settings that control the speed and size of objects (SpaceShip, bullets, Aliens, game speed)
 - spaceInvader.py
    - This will serve as the main file that brings in the functionality of other classes into one place. The way gets executed from here
 - spaceShip.py
    - SpaceShip object where bullets originate from. Sits at the bottom of the screen and moves from left to right.

Screenshots
![image](Screenshots/Screenshot%20(8).png "Start Game")
![image](Screenshots/Screenshot%20(9).png "Game")
![image](Screenshots/Screenshot%20(10).png "Game")
![image](Screenshots/Screenshot%20(11).png "Game")
![image](Screenshots/Screenshot%20(12).png "Game")

class Settings:
    # Class definition to store all game settings

    def __init__(self) -> None:
        # Initializing game static settings

        # Screen settings and color
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230, 230, 230)

        # Ship
        self.shipLimit = 3

        # Bullets
        self.bulletWidth = 5.0
        self.bulletHeight = 8.0
        self.bulletColor = (60, 60, 60)

        # Limit the amout of bullets
        self.bulletLimit = 5

        # Alien Settings
        self.fleetDropSpeed = 5

        # How fast the ships fall/game speed
        self.speedScale = 1.1

        # Score scale, faster = morepoints
        self.scoreScale = 1.5

        self.dynamicSettings()

    def dynamicSettings(self):
        # Game settings that change while playing as a way of intruducing game difficulty
        self.shipSpeed = 1.0
        self.bulletSpeed = 0.5
        self.alienSpeed = 0.5

        # Fleet direction of 1 represents right and -1 represnts lefs
        self.fleetDirection = 1

        # Scoring alien dead = 50pts
        self.alienPoints = 50

    def increaseSpeed(self):
        self.shipSpeed *= self.speedScale
        self.bulletSpeed *= self.speedScale
        self.alienSpeed *= self.speedScale

        self.alienPoints = int(self.alienPoints * self.scoreScale)

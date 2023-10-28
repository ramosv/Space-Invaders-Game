class Settings:
    #Class definition to store all game settings

    def __init__(self) -> None:
        #Initializing game settings

        #Screen settings and color
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230,230,230)

        #Ship
        self.shipSpeed = 1.0

        #Bullets
        self.bulletSpeed = .5
        self.bulletWidth = 2.0
        self.bulletHeight = 8.0
        self.bulletColor = (60,60,60)

        #Limit the amout of bullets
        self.bulletLimit = 5

        #Alien Settings
        self.alienSpeed = .5
        self.fleetDropSpeed = 5
        #Fleet direction of 1 represents right and -1 represnts lefs
        self.fleetDirection = 1
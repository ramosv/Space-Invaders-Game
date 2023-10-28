class Settings:
    #Class definition to store all game settings

    def __init__(self) -> None:
        #Initializing game settings

        #Screen settings and color
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230,230,230)

        self.shipSpeed = 1.0
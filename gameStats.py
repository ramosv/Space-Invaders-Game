class GameStats:
    def __init__(self, siGame):
        self.settings = siGame.settings
        self.resetStats()

        # Space invader is active = still alive
        self.gameActive = False

        self.highScore = 0

    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit
        self.score = 0
        self.level = 1

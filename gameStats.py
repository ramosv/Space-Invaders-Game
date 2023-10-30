class GameStats:
    def __init__(self, siGame):
        self.settings = siGame.settings
        self.resetStats()

        # Space invader is active = still alive
        self.gameActive = False

    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit

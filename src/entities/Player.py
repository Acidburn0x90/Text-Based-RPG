
class Player:
    def __init__(self):
        self.health = 100
        self.hpmax = 100
        self.inventory = []
        self.location = "Starting Point"
        self.money = 25
        self.level = 1
        self.experience = 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

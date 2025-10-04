from src.entities.Player import Player

class GameState:
    def __init__(self):
        self.player = Player()
        self.enemies = []
        self.locations = []
        
    def move_player(self, new_location):
        self.player.location = new_location
        

global_game_state = GameState()
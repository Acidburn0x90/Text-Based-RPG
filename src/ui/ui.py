import blessed
term = blessed.Terminal()
from src.entities.Player import Player
from src.core.game_state import global_game_state

class UI:
    def __init__(self):
        self.map_height = 42


    def draw_map_outline(self):
        print(term.home + term.clear + term.move_y(0))
        map_rows = 37
        map_cols = 75
        outline = "+" + "-" * (map_cols - 2) + "+"
        print(term.move_xy(0, 1) + term.center(outline, fillchar=" "))
        for i in range(map_rows - 2):
            line = "|" + " " * (map_cols - 2) + "|"
            print(term.move_xy(0, 2 + i) + term.center(line, fillchar=" "))
        print(term.move_xy(0, map_rows) + term.center(outline, fillchar=" "))

    def draw_map_area(self, map_str: str):
        if len(map_str) != 35 * 74:
            raise ValueError("map_str must be exactly 2590 characters (35 rows of 74 columns) got " + str(len(map_str)))
        for row in range(35):
            line = "|" + map_str[row * 74:(row + 1) * 74] + "|"
            print(term.move_xy(0, 2 + row) + term.center(line, fillchar=" "))
        
    
    def draw_status_bar(self):
        # Define the line number for the status bar
        bar_y = self.map_height - 5
        stats = f"{term.red}Health: {global_game_state.player.health}/{global_game_state.player.hpmax}{term.gold}    Gold:{global_game_state.player.money}{term.deepskyblue}    Location:{global_game_state.player.location}{term.snow}" 
        print(term.snow + term.move_xy(0, bar_y + 1) + term.center(stats, fillchar="-"))

    def draw_action_menu(self):
        menu_y = self.map_height - 4
    
        prompt = f"{term.height} + {term.width}"
        choices = "1) Move North   2) Check Inventory   3) Wait"
    
        print(term.move_xy(2, menu_y + 1) + term.bold(prompt))
        print(term.move_xy(2, menu_y + 2) + choices)

    




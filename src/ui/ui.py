import blessed
term = blessed.Terminal()
from src.core.database import Player

class UI:
    def __init__(self, user: Player):
        self.user = user


    def draw_map_area(self):
        map_height = term.height - 6
        print(term.home + term.clear + term.move_y(0)) # Move to the top
        for i in range(map_height):
            # This is where you would print each line of your map
            print(f"Map line {i} " + term.clear_eol)
    
    def draw_status_bar(self):
        # Define the line number for the status bar
        bar_y = term.height - 5
        stats = f"{term.red}Health: {self.user.hp}/{self.user.hpmax}{term.gold}    Gold:{self.user.money}{term.deepskyblue}    Location:{self.user.location}{term.snow}" 
        print(term.snow + term.move_xy(0, bar_y + 1) + term.center(stats, fillchar="-"))

    def draw_action_menu(self):
        menu_y = term.height - 4
    
        prompt = "What do you do?"
        choices = "1) Move North   2) Check Inventory   3) Wait"
    
        print(term.move_xy(2, menu_y + 1) + term.bold(prompt))
        print(term.move_xy(2, menu_y + 2) + choices)




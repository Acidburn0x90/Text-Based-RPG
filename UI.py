import blessed

term = blessed.Terminal()

# --- Game State Data (put your game variables here) ---
player_stats = {
    "max_hp": 100,
    "hp": 95,
    "money": 120,
    "location": "Whispering Woods"
}

def draw_map_area():
    """Draws the main game world view."""
    # For now, we'll just draw a placeholder box.
    # Later, you'll render your game map here.
    map_height = term.height - 6
    print(term.move_y(0)) # Move to the top
    for i in range(map_height):
        # This is where you would print each line of your map
        print(f"Map line {i}" + term.clear_eol)

def draw_status_bar():
    """Draws the player's health, money, and location."""
    # Define the line number for the status bar
    bar_y = term.height - 5
    stats = f"{term.red}Health: {player_stats["hp"]}/{player_stats["max_hp"]}{term.gold}    Gold:{player_stats['money']}{term.deepskyblue}    Location:{player_stats['location']}{term.snow}" 

    print(term.snow + term.move_xy(0, bar_y + 1) + term.center(stats, fillchar="-"))
    

def draw_action_menu():
    """Draws the available choices or messages for the player."""
    menu_y = term.height - 3
    
    prompt = "What do you do?"
    choices = "1) Move North   2) Check Inventory   3) Wait"
    
    print(term.move_xy(2, menu_y + 1) + term.bold(prompt))
    print(term.move_xy(2, menu_y + 2) + choices)


# --- Main Game Loop ---
def main():
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        key = ''
        while key.lower() != 'q':
            # 1. DRAW EVERYTHING
            print(term.home + term.clear) # Clear the screen
            draw_map_area()
            draw_status_bar()
            draw_action_menu()

            # 2. GET INPUT
            # Put game logic here to handle choices
            key = term.inkey()
from src.core.game_state import global_game_state
from src.ui.ui import UI

class GameEngine:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        
        while self.running:
            self.render()
            command = input("Enter command: ").strip().lower()
            if command in ['exit', 'quit']:
                self.stop()
            else:
                print(f"Unknown command: {command}")

    def stop(self):
        self.running = False

    def is_running(self):
        return self.running
    
    def render(self):
        renderer = UI()
        renderer.draw_map_area()
        renderer.draw_status_bar()
        renderer.draw_action_menu()

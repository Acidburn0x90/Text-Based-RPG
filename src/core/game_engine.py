from src.core.database import db, Player
from src.ui.ui import UI

class GameEngine:
    def __init__(self):
        self.running = False
        self.player = None

    def initialize(self):
        if db.is_closed():
            db.connect()
        db.create_tables([Player])

        self.player = Player.select().first()
        if not self.player:
            self.player = Player(name="Hero", level=1, experience=0)
            self.player.save()

    def start(self):
        self.initialize()
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
<<<<<<< HEAD

def initialize():
    if db.is_closed():
        db.connect()
    db.create_tables([Player])

    player = Player.select().first()
    if not player:
        player = Player(name="Hero", level=0, experience=0)
        player.save()

    print(f"Welcome back, {player.name}!")
    renderer = UI(player)
    renderer.draw_map_area()
    renderer.draw_status_bar()
    renderer.draw_action_menu()
=======
    
    def render(self):
        renderer = UI(self.player)
        renderer.draw_map_area()
        renderer.draw_status_bar()
        renderer.draw_action_menu()
>>>>>>> 191de0f0886fa5bfde0cddd6793cbf2d659def56

from src.core.database import db, Player
from src.ui.ui import UI

player = Player


def initialize():
    db.connect()
    db.create_tables([Player])

    player = Player.select().first()
    if not player:
        player = Player(name="Hero", level=0, experience=0)
        player.save()

    print(f"Welcome back, {player.name}!")
    renderer = UI()
    renderer.draw_map_area()

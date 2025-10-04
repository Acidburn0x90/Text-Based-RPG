from src.core.database import db, Player

player = Player

def initialize():
    db.connect()
    db.create_tables([Player])

    player = Player.select().first()
    if not player:
        player = Player(name="Hero", level=0, experience=0)
        player.save()

    print(f"Welcome back, {player.name}!")
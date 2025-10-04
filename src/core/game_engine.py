from src.core.database import db, Player

player = Player

def initialize():
    db.connect()
    db.create_tables([Player])

    player = Player.select().first()
    if not player:
        player = Player(name="Hero", level=0, experience=0)
        player.save()

<<<<<<< HEAD
    print(f"Welcome back, {player.name}!")
=======
    print(f"Welcome back, {user.name}!")
    renderer = UI()
    renderer.draw_map_area()
>>>>>>> a3f46a81de733ebdb9319b78a9bccb456eed1436

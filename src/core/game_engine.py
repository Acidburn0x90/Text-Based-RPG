from src.core.database import db, Player


def initialize():
    db.connect()
    db.create_tables([Player])

    user = Player.select().first()
    if not user:
        user = Player(name="Hero", level=0, experience=0)
        user.save()

    print(f"Welcome back, {user.name}!")
    renderer = UI()
    renderer.draw_map_area()
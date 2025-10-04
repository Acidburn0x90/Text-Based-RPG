from src.core.database import db, Player


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

        print(f"Welcome back, {self.player.name}!")

    def start(self):
        self.initialize()
        self.running = True

    def stop(self):
        self.running = False

    def is_running(self):
        return self.running


def initialize():
    if db.is_closed():
        db.connect()
    db.create_tables([Player])

    user = Player.select().first()
    if not user:
        user = Player(name="Hero", level=1, experience=0)
        user.save()

    print(f"Welcome back, {user.name}!")
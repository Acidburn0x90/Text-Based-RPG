import sys
import os
import asyncio
from UI import UI


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.game_engine import initialize

def main():
    initialize()
    
    #This is the main game loop, as of not the global DB will be used.
    while True:
     #This will halt until user input is received
     process_user_input()
     update_environment()
     generative_content()
     persist_environment()
     persist_environment()

async def initialize_from_persist_environment():
    db.connect()
    db.create_tables([Player])

    user = Player.select().first()

    if not user:
        user = Player(name="Hero", level=0, experience=0)
        user.save()


    print(f"Welcome back, {user.name}!")

    renderer = UI()
    renderer.draw_map_area()



    #Get secrets from .env 
def process_user_input():
    pass

def update_environment():
    pass

def generative_content():
    pass

def persist_environment():
    pass

if __name__ == "__main__":
    main()
import sys
import os

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
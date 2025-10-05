import sys
import os


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.game_engine import initialize

def main():
    initialize()
<<<<<<< HEAD
    
    #This is the main game loop, as of not the global DB will be used.
    while True:
     #This will halt until user input is received
     process_user_input()
     update_environment()
     generative_content()
     persist_environment()
     persist_environment()
    
=======

# def process_user_input():
#     pass

# def update_environment():
#     pass
>>>>>>> 964f53b378a0325dfbc56a3a11f9ae680bf42951

# def generative_content():
#     pass

# def persist_environment():
#     pass

if __name__ == "__main__":
    main()
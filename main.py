def main():
    initialize_from_persist_environment()
    #This is the main game loop, as of not the global DB will be used.
    while True:
     #This will halt until user input is received
     process_user_input()
     update_environment()
     generative_content()
     persist_environment()

    

if __name__ == "__main__":
    main()
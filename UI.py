import blessed

term = blessed.Terminal()

# Player's starting position
x, y = 10, 5

# Game loop
def main():
    global x, y # Use the global x and y variables

    # Use context managers to handle terminal state
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        # Clear the screen initially
        print(term.home + term.clear)

        key = ''
        # Main game loop: runs until 'q' is pressed
        while key.lower() != 'q':
            print(term.home + term.clear)
            # 1. DRAW THE SCENE
            # Clear previous player position by printing a space
            print(term.move_xy(x, y) + ' ')

            # Draw the player at the new position
            player_char = term.bold_yellow('@')
            print(term.move_xy(x, y) + player_char)

            # Draw instructions
            instructions = "Use arrow keys to move. Press 'q' to quit."
            print(term.move_xy(0, term.height - 1) + term.center(instructions))


            # 2. GET USER INPUT
            key = term.inkey() # Wait for a key press

            # 3. UPDATE GAME STATE
            if key.is_sequence:
                if key.name == "KEY_UP":
                    y -= 1
                elif key.name == "KEY_DOWN":
                    y += 1
                elif key.name == "KEY_LEFT":
                    x -= 1
                elif key.name == "KEY_RIGHT":
                    x += 1

            # Clamp player position to stay within screen bounds
            x = max(0, min(x, term.width - 1))
            y = max(0, min(y, term.height - 2)) # -2 to keep off instruction line


if __name__ == "__main__":
    main()
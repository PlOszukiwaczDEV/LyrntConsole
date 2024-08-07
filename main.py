import requests
import os
import json
from dotenv import load_dotenv
import curses

# headers
import utils.lynt as lynt
import wrapper.utils.headers as headdb

load_dotenv()

def run_menu(stdscr):
    # Clear screen
    stdscr.clear()

    # A list of menu options
    menu = ['Option 1', 'Option 2', 'Option 3', 'Exit']

    # Set the starting index for the selection
    current_row = 0

    while True:
        # Clear the screen
        stdscr.clear()

        # Display the menu options
        for idx, option in enumerate(menu):
            if idx == current_row:
                stdscr.addstr(idx, 0, option, curses.A_REVERSE)  # Highlight the current option
            else:
                stdscr.addstr(idx, 0, option)

        # Refresh the screen to show updates
        stdscr.refresh()

        # Get the user input
        key = stdscr.getch()

        # Handle user input
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[current_row] == 'Exit':
                break
            else:
                stdscr.clear()
                if menu[current_row] == 'Option 1':
                    stdscr.addstr(0, 0, "You've chosen Option 1!")
                elif menu[current_row] == 'Option 2':
                    stdscr.addstr(0, 0, "You've chosen Option 2!")
                elif menu[current_row] == 'Option 3':
                    stdscr.addstr(0, 0, "You've chosen Option 3!")
                stdscr.refresh()
                stdscr.getch()

    # End the curses session
    curses.endwin()

curses.wrapper(run_menu)
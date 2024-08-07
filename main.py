import requests
import os
import json
from dotenv import load_dotenv
from blessed import Terminal

# headers
import utils.lynt as lynt
import utils.headers as headdb

load_dotenv()

def run_menu(term):
    menu = ['Send a lynt', 'Like a lynt', 'Option 3', 'Exit']
    current_row = 0

    while True:
        with term.cbreak(), term.hidden_cursor():
            print(term.home + term.clear)

            # Display the menu options
            for idx, option in enumerate(menu):
                if idx == current_row:
                    print(term.reverse(option))
                else:
                    print(option)

            print(term.move_yx(term.height - 1, 0) + "Use arrow keys to move, Enter to select, 'q' to quit.")
            key = term.inkey()

            # Handle user input
            if key.name == 'KEY_UP' and current_row > 0:
                current_row -= 1
            elif key.name == 'KEY_DOWN' and current_row < len(menu) - 1:
                current_row += 1
            elif key == 'q':
                break
            elif key.name == 'KEY_ENTER':
                if menu[current_row] == 'Exit':
                    break  # Exit the application
                else:
                    handle_option(term, menu[current_row])

def handle_option(term, option):
    with term.cbreak(), term.hidden_cursor():
        print(term.home + term.clear)

        if option == 'Send a lynt':
            prompt = "Enter your message: "
            prompt2 = "\nEnter the ID of the message to repost (optional): "
            print(prompt, end='', flush=True)
            user_input = capture_input(term)
            print(prompt2, end='', flush=True)
            repostid = capture_input(term)
            
            r = lynt.send_lynt(user_input, repostid)
            print(f"\nStatus Code: {r.status_code}")
            print(f"\nResponse: {r.text}")
        elif option == 'Like a lynt':
            prompt = "Enter the ID of the message to like: "
            print(prompt, end='', flush=True)
            user_input = capture_input(term)
            
            r = lynt.like_lynt(user_input)
            print(f"\nStatus Code: {r.status_code}")
            print(f"\nResponse: {r.text}")
        else:
            print(f"You've chosen {option}!")

        print(term.move_yx(term.height - 1, 0) + "Press any key to return to the menu.")
        term.inkey()  # Wait for another key press before returning to the menu

def capture_input(term):
    """ Captures multi-character input from the user """
    buffer = []
    while True:
        key = term.inkey()
        if key.name == 'KEY_ENTER':
            break
        elif key.name == 'KEY_BACKSPACE':
            if buffer:
                buffer.pop()
                print(' ', end='', flush=True)
        elif key:
            buffer.append(key)
            print(key, end='', flush=True)

    return ''.join(buffer)

if __name__ == '__main__':
    term = Terminal()
    run_menu(term)
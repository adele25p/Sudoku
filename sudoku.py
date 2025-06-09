""" Main file for the Sudoku game.
This script serves as the entry point for the Sudoku game, allowing users to choose between a CLI or a GUI to play the game.
It also allows users to select the difficulty level of the game.
It uses argparse for command-line argument parsing and provides a simple user interface.
"""

# import necessary libraries
import argparse
import subprocess

# import necessary modules
from cli import *
from gui import *

# Constants for difficulty levels and quit commands
DIFFICULTY_LEVEL = ['easy', 'medium', 'hard']
QUIT_COMMANDS = ['q', 'quit']

def prompt_choice(prompt, choices):
    """Prompt the user to choose an option from a list of choices.
    Args:
        prompt (str): The prompt message to display to the user.
        choices (list): A list of valid choices.
    Returns:
        str: The user's choice if valid, otherwise None.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        elif choice in QUIT_COMMANDS:
            print("Exiting the game.")
            return None
        else:
            print(f"Invalid choice. Please choose from {', '.join(choices)} or enter 'q' to quit.")

def main():
    """Main function to run the Sudoku game.
    This function handles the command-line interface and user input to start the game.
    It allows the user to choose between CLI and GUI modes, as well as the difficulty level.
    It also provides a version option to display the game's version.
    """

    # Parse command-line arguments using argparse
    parser = argparse.ArgumentParser(description="Sudoku Game")
    parser.add_argument('-v', '--version', action='version', version='Sudoku Game 1.0', help='Show the version of the Sudoku game')
    parser.add_argument('--cli', action='store_true', help='Run the game in CLI mode')
    parser.add_argument('-t', '--test', '--tests', action='store_true', help='Run the game in test mode (CLI only)')
    args = parser.parse_args()

    level = None
    if not args.tests:
        # Check if the user wants to play in a specific difficulty level
        level = prompt_choice(f"Choose difficulty level ({', '.join(DIFFICULTY_LEVEL)}): ", DIFFICULTY_LEVEL)
        if level is None:
            return

    # Run the game in the selected mode and difficulty level
    if args.cli:
        print(f"Running Sudoku in CLI mode with {level} difficulty...")
        run_cli(level)
    elif args.tests:
        print("Running Sudoku in test mode (CLI only)...")
        subprocess.run(['pytest'])
    else:
        print(f"Running Sudoku in GUI mode with {level} difficulty...")
        run_gui(level)

if __name__ == "__main__":
    main()
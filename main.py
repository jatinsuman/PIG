import random
from colorama import init
init()
from colorama import Fore, Back, Style
import sys

player_score = 0
computer_score = 0

die_roll = 0
die_count = 0
die_roll_count = None

turn = "player"

print(Fore.YELLOW + Style.BRIGHT + "Enter any key to roll die again, Enter 's' to add count to score")

while True:
    if turn == "player":
        print(Fore.GREEN + f"player score: {player_score}  computer score: {computer_score}")

        while turn == "player":
            die_roll = random.choice([2, 3, 4, 1, 5, 6])
            if die_roll != 1:
                die_count += die_roll
                p_count = input(Fore.BLACK + Back.BLUE + f" {die_count} " + Back.RESET)
                
                if p_count.lower() == "s":
                    player_score += die_count
                    if player_score >= 100:
                        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f"Player wins {player_score} - {computer_score}")
                        sys.exit()
                    turn = "computer"
                    die_count = 0
                    print(Fore.YELLOW + "Count added to your score. Now it's the computer's turn")
            else:
                die_count = 0
                print(Fore.YELLOW + "The die rolled 1. It is now the computer's turn...")
                turn = "computer"
                input("")

    elif turn == "computer":
        print(Fore.GREEN + f"player score: {player_score}  computer score: {computer_score}")

        while turn == "computer":
            die_roll = random.choice([1, 2, 3, 4, 5, 6])
            if die_roll != 1:
                die_count += die_roll
                c_count = input(Fore.WHITE + Back.RED + f" {die_count} " + Back.RESET)
                
                die_roll_count = random.choice([0, 0, 0, "s"])
                if die_roll_count == "s":
                    computer_score += die_count
                    if computer_score >= 100:
                        print(Fore.LIGHTRED_EX + Style.BRIGHT + f"Computer wins {computer_score} - {player_score}")
                        sys.exit()
                    turn = "player"
                    die_count = 0
                    print(Fore.YELLOW + "Computer added count to it's score. Now it's your turn")
            else:
                die_count = 0
                print(Fore.YELLOW + "The die rolled 1. It is now your turn...")
                turn = "player"
                input("")

# -*- coding: utf-8 -*-
"""
Created on 2023-08-11

@author: Zoey Striker

Description:
    Basic graphics for the main file to display.
"""

# % IMPORT DEPENDENCIES AND SETTINGS AND GLOBAL VARIABLES
from Player import Player

LOGO = """
.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'
"""


# % FUNCTIONS
def announce_winner(outcome: str):
    """
    Announces winner in plain text.

    Parameters
    ----------
    outcome : str
        Plain text of which player one or other descriptors for the outcome
        of a game of blackjack.

    Returns
    -------
    Prints to screen.

    """
    if outcome == 'draw':
        print('It\'s a draw!')
    elif outcome == 'blackjack':
        print('You got Blackjack!')
    else:
        print(f'{outcome} is the winner!')


def main_menu(options: dict, player: Player):
    """
    Prints the main menu of the Blackjack game.

    Parameters
    ----------
    options : dict
        Each option with it's associated text key and item function.
    player : player
        User's information as a player object.

    Returns
    -------
    Prints to screen.

    """
    print(LOGO)

    print(f"{'Welcome ' + player.name + '!':^72}")
    print(f"{'Current Chips: ' + str(player.chips):^72}")
    print('\n' + '-' * 72 + '\n')

    for option, info in options.items():
        print(f"{option}: {info['text']}")


def player_turn(options: dict, player: Player, dealer: Player):
    """


    Parameters
    ----------
    options : dict
        Each option with it's associated text key and item function.
    player : Player
        Player object representing the user.
    dealer : Player
        Player object representing the dealer.

    Returns
    -------
    Prints to screen.

    """
    print(dealer)
    print('-' * 20)
    print(player)

    for option, info in options.items():
        print(f"{option}: {info['text']}")


# %% MAIN
def main():
    pass


if __name__ == '__main__':
    main()

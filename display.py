# -*- coding: utf-8 -*-
"""
Created on 2023-08-11

@author: Zoey Striker

Description:
    What this program does!
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
def main_menu(options: dict):
    print(LOGO)

    for option, info in options.items():
        print(f"{option}: {info['text']}")


def player_turn(options: dict, player: Player, dealer: Player):
    print(dealer)
    print('-' * 20)
    print(player)

    for option, info in options.items():
        print(f"{option}: {info['text']}")


# % MAIN
def main():
    pass


if __name__ == '__main__':
    main()

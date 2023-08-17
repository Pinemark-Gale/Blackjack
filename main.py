# -*- coding: utf-8 -*-
"""
Created on 2023-08-11

@author: Zoey Striker

Description:
    What this program does!
"""

# %% IMPORT DEPENDENCIES AND SETTINGS
from PlayingDeck import PlayingDeck
from PlayingCard import PlayingCard
from Player import Player

import display
import os
import game_logic as gl

player_name = 'Player'
blank = PlayingCard("0", " ")
dealer = Player('Dealer')
player = Player('Player')
deck = PlayingDeck(simple_face=True)


# %% FUNCTIONS
def draw_player():
    player.pickup(deck.draw())


def draw_dealer():
    dealer.pickup(deck.draw())


def end_game():
    print('Results:', gl.outcome(player, dealer))

    player.chips = player.chips + \
        gl.payout(gl.outcome(player, dealer), 100, player, dealer)
    print('Player Chips:', player.chips)


def exit_game() -> None:
    print('Exiting game...')

    return None


def load_save() -> None:
    pass


def set_player_name():
    player.name(input('Please enter player name: '))


def start_game() -> None:
    player.pickup(deck.draw())
    dealer.pickup(deck.draw())
    player.pickup(deck.draw())

    choice = 0
    menu_items = {
        1: {'text': 'Hit', 'item': draw_player},
        2: {'text': 'Stand', 'item': end_game},
        3: {'text': 'Quit', 'item': menu}
    }

    while gl.is_under(player) and choice != 2:
        display.player_turn(menu_items, player, dealer)
        choice = int(input('\nEnter number: '))

        menu_items[choice]['item']()


def menu() -> None:
    choice = 0

    menu_items = {
        1: {'text': 'Start Game', 'item': start_game},
        2: {'text': 'Load Save', 'item': load_save},
        3: {'text': 'Set Player Name', 'item': set_player_name},
        4: {'text': 'Quit', 'item': exit_game}
    }

    display.main_menu(menu_items)

    while choice not in menu_items.keys():
        choice = int(input('\nEnter number: '))

    menu_items[choice]['item']()

    return choice

# %% MAIN


def main():

    while menu() != 4:
        pass


if __name__ == '__main__':
    main()

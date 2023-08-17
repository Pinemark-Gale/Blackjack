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
import time
import game_logic as gl

player_name = 'Player'
blank = PlayingCard("0", " ")
dealer = Player('Dealer')
player = Player('Player')
bet = 0
deck = PlayingDeck(simple_face=True)
deck.shuffle()


# %% FUNCTIONS
def draw_player():
    player.pickup(deck.draw())


def draw_dealer():
    dealer.pickup(deck.draw())


def end_game():
    # Play dealer's turn.
    while gl.is_under(dealer, max_score=17) and gl.is_under(player, max_score=21):
        draw_dealer()

    # Announce winner.
    time.sleep(1)
    display.player_turn({}, player, dealer)
    time.sleep(3)
    display.announce_winner(gl.outcome(player, dealer))

    # Calculate payout.
    player.chips = player.chips + \
        gl.payout(gl.outcome(player, dealer), bet, player, dealer)
    print('Player Chips:', player.chips)
    time.sleep(4)

    player.export()
    reset_game()


def exit_game() -> None:
    print('Exiting game...')

    return None


def load_save() -> None:
    stats = None

    with open('player.txt') as f:
        stats = f.read().split(',')

    player.name = str(stats[0])
    player.chips = int(stats[1])


def reset_game():
    global deck
    global bet
    bet = 0
    player.reset_hand()
    dealer.reset_hand()
    deck = PlayingDeck(simple_face=True)
    deck.shuffle()


def set_player_name():
    player.name = input('Please enter player name: ')


def start_game() -> None:
    global bet

    while bet <= 0 or bet > player.chips:
        bet = gl.get_number(
            'How many chips would you like to bet? (Press Enter to bet 20.) ',
            default=20,
        )

    player.pickup(deck.draw())
    dealer.pickup(deck.draw())
    player.pickup(deck.draw())

    choice = 0
    menu_items = {
        1: {'text': 'Hit', 'item': draw_player},
        2: {'text': 'Stand', 'item': print},
        3: {'text': 'Quit', 'item': menu}
    }

    while gl.is_under(player) and choice != 2:
        display.player_turn(menu_items, player, dealer)
        choice = gl.get_number('\nEnter number: ', 0)

        menu_items[choice]['item']()

    end_game()


def menu() -> None:
    choice = 0

    menu_items = {
        1: {'text': 'Start Game', 'item': start_game},
        2: {'text': 'Load Save', 'item': load_save},
        3: {'text': 'Set Player Name', 'item': set_player_name},
        4: {'text': 'Quit', 'item': exit_game}
    }

    display.main_menu(menu_items, player)

    while choice not in menu_items.keys():
        choice = gl.get_number(
            prompt='\nEnter number: ',
            default=1,
        )

    menu_items[choice]['item']()

    if player.chips <= 0:
        print('Oh no! You ran out of chips. Game over!')
        choice = 4

    return choice


# %% MAIN
def main():

    while menu() != 4:
        pass


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""
Created on 2023-08-17

@author: Zoey Striker

Description:
    What this program does!
"""

# % IMPORT DEPENDENCIES AND SETTINGS
from PlayingDeck import PlayingDeck
from PlayingCard import PlayingCard
from Player import Player
import random


# % FUNCTIONS
def is_blackjack(player: Player) -> bool:
    blackjack = False

    if len(player.hand) == 2:
        ranks = []

        for card in player.hand:
            ranks.append(card.rank)

        if 'A' in ranks and ('10' in ranks or 'J' in ranks or 'Q' in ranks or
                             'K' in ranks):
            blackjack = True

    return blackjack


def is_under(player: Player, max_score=21) -> bool:
    return max(player.total) <= max_score or min(player.total) <= max_score


def max_valid_score(player: Player, max_score=21) -> int:
    valid = 0

    if max(player.total) <= max_score:
        valid = max(player.total)
    elif min(player.total) <= max_score:
        valid = min(player.total)

    return valid


def outcome(player_1: Player, player_2: Player) -> str:
    winner = player_2.name
    p1_score = max_valid_score(player_1)
    p2_score = max_valid_score(player_2)

    if is_under(player_1):
        # player 2 total must be under 21
        if not is_under(player_2):
            winner = player_1.name

        # player 2 has less total
        if p1_score > p2_score:
            winner = player_1.name

        # player 1 has blackjack
        if is_blackjack(player_1):
            winner = 'blackjack'

        # draw if players have same value
        if p1_score == p2_score:
            winner = 'draw'

    return winner


def payout(outcome: str, bet: int, player_1: Player, player_2: Player) -> int:
    outcomes = {
        player_1.name: bet * 2,
        player_2.name: 0,
        'draw': bet,
        'blackjack': (bet * 2) + (bet * 1.5)
    }

    return outcomes[outcome]


# % MAIN
def main():
    player = Player(name='Player')
    dealer = Player(name='Dealer')
    deck = PlayingDeck(simple_face=True)
    deck.shuffle()

    player.pickup(deck.draw())
    dealer.pickup(deck.draw())
    player.pickup(deck.draw())
    dealer.pickup(deck.draw())

    for index in range(0, random.randint(1, 2)):
        if random.randint(1, 2) == 1 and max_valid_score(player) < 17:
            player.pickup(deck.draw())
        if random.randint(1, 2) == 1 and max_valid_score(dealer) < 17:
            dealer.pickup(deck.draw())

    print(player)
    print(dealer)

    print('Checking Blackjack...')
    print('# Player:', is_blackjack(player))
    print('# Dealer', is_blackjack(dealer))
    print('Checking winner...')
    print('#', outcome(player, dealer))
    print('Checking if is under...')
    print('# Player:', is_under(player))
    print('# Dealer:', is_under(dealer))
    print('Payout...')
    print('#', payout(outcome(player, dealer), 100, player, dealer))


if __name__ == '__main__':
    main()

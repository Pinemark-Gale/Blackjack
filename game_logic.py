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
    """
    Tests whether or not a given hand is a Blackjack hand.

    Parameters
    ----------
    player : Player
        A player object with a hand. Assuming hand is not empty.

    Returns
    -------
    bool
        True if hand consists of a Blackjack, false otherwise.

    """
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
    """
    Tests whether or not a given hand is under or equal to the given score.

    Parameters
    ----------
    player : Player
        Player object with the associated hand.
    max_score : int, optional
        The score to be less than or equal to. The default is 21.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    return max(player.total) <= max_score or min(player.total) <= max_score


def max_valid_total(player: Player, max_score=21) -> int:
    """
    Takes all totals associated with a player and checks which one is largest
    within the specified (inclusive) bounds.

    Parameters
    ----------
    player : Player
        Player object with the associated hand total.
    max_score : int, optional
        The score the total can meet but not exceed. The default is 21.

    Returns
    -------
    int
        DESCRIPTION.

    """
    valid = 0

    if max(player.total) <= max_score:
        valid = max(player.total)
    elif min(player.total) <= max_score:
        valid = min(player.total)

    return valid


def outcome(player_1: Player, player_2: Player) -> str:
    """
    String description of either the player name that one or other descriptors
    for other outcomes of the game (draw or blackjack).

    Parameters
    ----------
    player_1 : Player
        Player object that must beat the other player's total.
    player_2 : Player
        Player object that must defend against other player's total.

    Returns
    -------
    str
        Name of the outcome (either player name or descriptor).

    """
    winner = player_2.name
    p1_score = max_valid_total(player_1)
    p2_score = max_valid_total(player_2)

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
    """
    Calculates total number of chips to add or take away from the original
    pool of chips. Assumes that chips were not taken out of original pool
    before making calculations.

    Parameters
    ----------
    outcome : str
        From the outcome function, describing which player won or other
        descriptor.
    bet : int
        Number of chips bet for the particular round.
    player_1 : Player
        Player object who is trying to beat the dealer.
    player_2 : Player
        Player object who is the dealer.

    Returns
    -------
    int
        DESCRIPTION.

    """
    outcomes = {
        player_1.name: bet,
        player_2.name: -bet,
        'draw': 0,
        'blackjack': (bet * 1.5)
    }

    return outcomes[outcome]


# % MAIN
def main():
    # Declaring variables.
    player = Player(name='Player')
    dealer = Player(name='Dealer')
    deck = PlayingDeck(simple_face=True)
    deck.shuffle()

    # Dealing game.
    player.pickup(deck.draw())
    dealer.pickup(deck.draw())
    player.pickup(deck.draw())
    dealer.pickup(deck.draw())

    for index in range(0, random.randint(1, 2)):
        if random.randint(1, 2) == 1 and max_valid_total(player) < 17:
            player.pickup(deck.draw())
        if random.randint(1, 2) == 1 and max_valid_total(dealer) < 17:
            dealer.pickup(deck.draw())

    # Running tests.
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

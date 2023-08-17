# -*- coding: utf-8 -*-
"""
Created on 2023-08-11

@author: Zoey Striker

Description:
    Defines the playing card class allowing a user to create a playing card,
    display the card, and retrieve any values needed from that playing card
    including rank and suit.
"""

# %% IMPORT DEPENDENCIES AND SETTINGS


# %% FUNCTIONS
def translate_rank(rank: str, aces_high=False, simple_face=False) -> int:
    """
    Takes the rank of a card (number or letter) and translates that rank into
    a value.

    Parameters
    ----------
    rank : str
        The value you would see on a playing card (2-10, A, J, Q, or K).
    aces_high : bool, optional
        Whether or not an ace is considered a 1 or 14. The default is False.

    Returns
    -------
    int
        The number value of a card.

    """
    translated = None

    if rank.isdigit():
        translated = int(rank)
    else:
        if simple_face:
            value_map = {
                'A': 1,
                'J': 10,
                'Q': 10,
                'K': 10,
            }
        else:
            value_map = {
                'A': 1,
                'J': 11,
                'Q': 12,
                'K': 13,
            }

        translated = value_map[rank[:1]]

        if aces_high and translated == 1:
            translated = 14

    return translated


def translate_suit(suit: str) -> str:
    """
    Takes the written suit of a card and translates it into the utf-8 
    character.

    Parameters
    ----------
    suit : str
        The suit. Can spell out the suit or just include the first character
        of that suit name (diamond, club, spade, heart).

    Returns
    -------
    str
        The UTF-8 character of that suit.

    """
    value_map = {
        'd': chr(9670),
        'c': chr(9827),
        's': chr(9824),
        'h': chr(9829)
    }

    return value_map.get(suit[:1].lower(), ' ')


# %% CLASS
class PlayingCard:
    def __init__(self, rank: str, suit: str, aces_high=False,
                 simple_face=False):
        """
        Initialize the playing card with a rank and suite specified.

        Parameters
        ----------
        rank : str
            The rank of the card (2-10, A, J, Q, K).
        suit : str
            The name of the suit. Can use the first letter of the suit or
            use the full name of the suit (only checking for first letter).
        aces_high : bool, optional
            Specify whether or no the value of an ace should be 1 or 14. Often
            used in games like Texas Hold'em. The default is False.
        simple_face : bool, optional
            Will set all face cards to be a value of 10. Often seen in games
            like Blackjack and Cribbage.

        Returns
        -------
        None.

        """
        self.suit = translate_suit(suit)
        self.rank = rank[:2]
        self.value = translate_rank(rank, aces_high, simple_face)

    def __str__(self):
        """
        Generate an UTF-8 image of the card in the form of a string. Takes 5
        lines and seven characters in width. Best used with print function.

        Returns
        -------
        str
            Image of the card.

        """
        return '*- - -*' \
            + f'\n|{self.suit:>5}|' \
            + f'\n|{self.rank:^5}|' \
            + f'\n|{self.suit:<5}|' \
            + '\n*- - -*'

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __add__(self, other):
        if type(other) == PlayingCard:
            return self.value + other.value
        elif type(other) == int:
            return self.value + other


# %% MAIN
def main():
    # Basic testing of class functions.
    card = PlayingCard('2', 'd')
    print(f'Value: {card.value}')
    print(card)

    card = PlayingCard('J', 'diamonds')
    print(f'Value: {card.value}')
    print(card)

    card = PlayingCard('J', 'diamonds', simple_face=True)
    print(f'Value: {card.value}')
    print(card)

    card = PlayingCard('7', 'club')
    print(f'Value: {card.value}')
    print(card)

    card = PlayingCard('A', 's', True)
    print(f'Value: {card.value}')
    print(card)

    card = PlayingCard('10', 'H', True)
    print(f'Value: {card.value}')
    print(card)


if __name__ == '__main__':
    main()

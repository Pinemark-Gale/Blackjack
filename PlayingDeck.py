# -*- coding: utf-8 -*-
"""
Created on 2023-08-11

@author: Zoey Striker

Description:
    Creates a playing card deck class with the ability to create the deck,
    shuffle, draw, etc.
"""

# %% IMPORT DEPENDENCIES AND SETTINGS AND CONSTANTS
from PlayingCard import PlayingCard
from random import shuffle

DECK_MAX = 52


# %% FUNCTIONS
def value_to_rank(value: int) -> str:
    """
    Converts a value of a card to a rank in single character form.

    Parameters
    ----------
    value : int
        The number value of a card. Either the number on the card, or the
        equivalent (for example, J would be 11).

    Returns
    -------
    str
        The rank in string form.

    """
    rank = None

    value_map = {
        1: 'A',
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A'
    }

    rank = value_map.get(value, str(value))

    return rank


# %% CLASS
class PlayingDeck:
    def __init__(self, aces_high=False):
        """
        Initialize a deck of playing cards

        Parameters
        ----------
        aces_high : TYPE, optional
            DESCRIPTION. The default is False.

        Returns
        -------
        None.

        """
        suits = ['s', 'c', 'h', 'd']
        counter = -1
        self.deck = []

        for num in range(0, 52):
            if num % 13 == 0:
                counter += 1

            self.deck.append(
                PlayingCard(
                    value_to_rank(num % 13 + 1),
                    suits[counter],
                    aces_high=aces_high
                )
            )

    def draw(self, number=1) -> PlayingCard:
        """
        Draw the specified number of cards from the deck.

        Parameters
        ----------
        number : int, optional
            The number of cards you want to draw from the deck. 
            The default is 1.

        Returns
        -------
        PlayingCard
            The playing card that has been drawn from the deck.

        """
        cards = []

        for index in range(0, number):
            cards.append(self.deck.pop(0))

        if len(cards) == 1:
            cards = cards[0]

        return cards

    def shuffle(self):
        shuffle(self.deck)

    def __str__(self):
        output = ""

        for index, card in enumerate(self.deck):
            output += f'{card.rank + card.suit:>4}'

            if (index + 1) % 13 == 0:
                output += '\n'

        return output

    def __len__(self):
        return len(self.deck)


# %% MAIN
def main():
    print('Initializing deck...')
    deck = PlayingDeck()
    print(deck)

    print('\nShuffling deck...')
    deck.shuffle()
    print(deck)

    print('\nDrawing card from top of deck...')
    card = deck.draw()
    print(card)
    print(f'{len(deck)} cards remaining.')

    print('\nDrawing five cards from top of deck...')
    cards = deck.draw(5)
    print(*cards, sep='\n')
    print(f'{len(deck)} cards remaining.')

    print('\nMaking comparisons...')
    print(
        f'Is {cards[0].rank} less than {cards[1].rank}? {cards[0] < cards[1]} '
    )
    print(
        f'Is {cards[2].rank} greater than {cards[3].rank}? {cards[2] > cards[3]} '
    )
    print(
        f'Is {cards[3].rank} equal to {cards[4].rank}? {cards[3] == cards[4]} '
    )


if __name__ == '__main__':
    main()

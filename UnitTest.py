# -*- coding: utf-8 -*-
"""
Created on 2023-08-11

@author: Zoey Striker

Description:
    Unit tests the PlayingCard and PlayingDeck Classes.
"""

# % IMPORT DEPENDENCIES AND SETTINGS
from PlayingCard import PlayingCard as Card
from PlayingDeck import PlayingDeck as Deck
import unittest


# % TESTING
class TestStringMethods(unittest.TestCase):

    # TESTING PLAYING CARDS
    def test_playing_card(self):
        card = Card('Q', 's')
        self.assertEqual(card.value, 12, 'Value not calculated correctly.')
        self.assertEqual(card.rank, 'Q', 'Rank not recorded correctly.')
        self.assertEqual(card.suit, chr(9824), 'Suit not correct icon.')

    def test_operators(self):
        card_greater = Card('4', 'hearts')
        card_lesser = Card('A', 'club')
        card_equal = Card('4', 'd')

        self.assertGreater(card_greater, card_lesser,
                           'Greater than comparison failed.')
        self.assertLess(card_lesser, card_greater,
                        'Less than comparison failed.')
        self.assertEqual(card_greater, card_equal, 'Equal comparison failed.')

    # TESTING ALL PLAYING DECK
    def test_length(self):
        deck = Deck()
        self.assertEqual(len(deck), 52, 'Length is not calculating correctly.')

    def test_deck_single_draw(self):
        deck = Deck()
        deck.draw()

        self.assertEqual(len(deck), 51, 'Single card was not drawn!')

    def test_deck_multi_draw(self):
        deck = Deck()
        deck.draw(5)

        self.assertEqual(len(deck), 47, 'Five cards were not drawn!')

    def test_shuffle(self):
        deck_control = Deck()
        deck_shuffle = Deck()
        deck_shuffle.shuffle()

        self.assertNotEqual(
            deck_control.draw(),
            deck_shuffle.draw(),
            '1 in 52 chance this fails due to probability.'
        )


# % MAIN
if __name__ == '__main__':
    unittest.main()

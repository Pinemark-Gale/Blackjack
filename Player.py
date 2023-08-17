# -*- coding: utf-8 -*-
"""
Created on 2023-08-11

@author: Zoey Striker

Description:
    Defines the player class for Blackjack.
"""

# %% IMPORT DEPENDENCIES AND SETTINGS
from PlayingCard import PlayingCard
from PlayingDeck import PlayingDeck


# %% CLASS
class Player:
    def __init__(self, name: str, chips=100):
        """
        Initialize the player, requiring that a name is given.

        Parameters
        ----------
        name : str
            Name of the player.

        Returns
        -------
        None.

        """
        self.name = name
        self.hand = []
        self.total = [0, 0]
        self.chips = chips

    def pickup(self, card: PlayingCard):
        """
        Put the given card into the players hand and calculate the total.

        Parameters
        ----------
        card : PlayingCard
            Playing card to be added to the players hand..

        Returns
        -------
        Modifies values within class (total and hand).

        """
        # add card to hand
        self.hand.append(card)

        # recalculate total min and max value of hand
        total = [0, 0]
        for card in self.hand:
            total[0] += card.value
            total[1] += card.value

            # need to calculate all possible values if ace in hand
            if card.rank == 'A':
                total[1] += 10

        self.total = total

    def reset_hand(self):
        """
        Resets variables associated with the hand of a player.

        Returns
        -------
        None.

        """
        self.hand = []
        self.total = [0, 0]

    def export(self):
        """
        Exports variables into a text file.

        Returns
        -------
        None.

        """
        with open('player.txt', 'w') as f:
            f.write(f'{self.name}, {self.chips}')

    def __str__(self):
        """
        Outputs the player's name, total points, and visuals for all cards
        in a horizontal format.

        Returns
        -------
        output : str
            String that can be printed.

        """
        # give player information
        output = f' {self.name}'

        if self.total[0] == self.total[1]:
            output = output + f' | Points: {self.total[0]}'
        else:
            output = output + f' | Points: {self.total}'

        # give all card values horizontally
        lines = ['', '', '', '', '']
        for card in self.hand:
            for index, card_line in enumerate(str(card).split('\n')):
                lines[index] = lines[index] + ' ' + card_line

        for line in lines:
            output = output + '\n' + line

        return output


# %% MAIN
def main():
    # Declare variables.
    deck = PlayingDeck(simple_face=True)
    deck.shuffle()

    player = Player('Player')

    # Basic testing.
    player.pickup(deck.draw())
    player.pickup(deck.draw())
    print(player)

    player.pickup(deck.draw())
    print(player)


if __name__ == '__main__':
    main()

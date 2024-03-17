import random
import itertools

class Deck:
    """Creating the deck with randomly shuffled 52 cards."""

    suits = ['\u2666', '\u2665', '\u2663', '\u2660']  # ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=0, rank=0, initial_cards = []) -> None:
        """Default constructor"""
        self.suit = suit
        self.rank = rank
        self.initial_cards = initial_cards

    def reset(self) -> None:
        """Reseting the deck."""
        self.initial_cards = list(itertools.product(self.suits, self.ranks))

    def shuffle(self) -> list :
        """Shuffling the deck."""
        random.shuffle(self.initial_cards)
        return self.initial_cards

    def __str__(self, list_=[]) -> str:
        """Changing the cards list to human readable form."""
        return ''.join([f'{suit}{value} ' for suit, value in list_])[:-1]


class Hand(Deck):
    def __init__(self, player_1='', player_2='', player_3='', player_4=''):
        super().__init__()
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_3 = player_3
        self.player_4 = player_4

    def distribute(self):
        """Distributing the cards."""
        self.reset()
        shuffled_cards = self.shuffle()
        self.player_1, self.player_2, self.player_3, self.player_4 = [shuffled_cards[i::4] for i in range(4)]

        self.player_1 = list(self.__str__(self.player_1).split(" "))
        self.player_2 = self.__str__(self.player_2)
        self.player_3 = self.__str__(self.player_3)
        self.player_4 = self.__str__(self.player_4)

        # print(self.__str__('DECK :- ', shuffled_cards))
        # print(self.__str__('Player 1 :- ',player_1))
        # print(self.__str__('Player 2 :- ',player_2))
        # print(self.__str__('Player 3 :- ',player_3))
        # print(self.__str__('Player 4 :- ',player_4))


class Rules(Hand):
    def __init__(self, throw_card='', round_card=[]):
        super().__init__()
        super().distribute()
        self.throw_card = throw_card
        self.round_card = round_card

    def round_shape(self) -> str:
        """Shape of the card thrown initially in first round."""
        return self.round_card[0][0]

    def throw_shape_status(self) -> bool:
        """Checks if the throw_card matches the playing round shape or not"""
        return True if self.throw_card == self.round_shape() or self.throw_card == '\u2660' else False



    def playcard(self):
        pass

    def wincard(self):
        pass


if __name__ == "__main__":
    rules = Rules()
    rules.throw_shape_status()

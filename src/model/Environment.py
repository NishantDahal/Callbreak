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

    def __str__(self, holder_name='',list_=[]) -> str:
        """Changing the cards list to human readable form."""
        return f'{holder_name}'+''.join([f'{suit}{value} ' for suit, value in list_])




class Hand(Deck):
    def __init__(self, players_hand=[]):
        super().__init__()
        self.players_hand = players_hand

    def distribute(self):
        """Distributing the cards."""
        self.reset()
        shuffled_cards = self.shuffle()
        player_1, player_2, player_3, player_4 = [shuffled_cards[i::4] for i in range(4)]
        print(shuffled_cards)
        print(self.__str__('DECK :- ', shuffled_cards))
        print(self.__str__('Player 1 :- ',player_1))
        print(self.__str__('Player 2 :- ',player_2))
        print(self.__str__('Player 3 :- ',player_3))
        print(self.__str__('Player 4 :- ',player_4))

if __name__ == "__main__":
    hand = Hand()
    hand.distribute()

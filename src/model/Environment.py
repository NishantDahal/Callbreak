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
    def __init__(self, throw='', round=[], priority=[]):
        super().__init__()
        self.throw = self.card_played() #This calls the method from the child class -> Play
        self.round = round
        self.priority = priority # This will be used to determine the winner of the round

    def first_or_not(self):
        """Checks if the card played is the first card played in the round or not"""
        if not round:
            return True
        else:
            return False

    def initiate_shape(self):
        """Checks if the round is being played in correct suit or not."""
        if not self.first_or_not:
            if self.round[0][0] == self.throw[0]:
                return True
        else:
                return False


    def higher_rank(self):
        """Checks if the player is throwing higher rank card than before or not."""
        if not self.first_or_not:
            if self.ranks.index(self.throw[1:]) > self.ranks.index(self.round[-1][1:]):
                self.priority.append(self.ranks.index(self.throw[1:]))
                return True


    def allow_spade(self):


    def any_card(self):
        pass

    def card_played(self):
        pass


class Play(Rules):
    def __init__(self, throw='', turn=1, current_bid=[0, 0, 0, 0], total_bid=[0, 0, 0, 0], achieved_bid=[0, 0, 0, 0]):
        super().__init__()
        self.throw = throw
        self.turn = turn
        self.current_bid = current_bid
        self.total_bid = total_bid
        self.achieved_bid = achieved_bid

    def initiate_turn(self) -> int:
        """Randoming first player to throw or bid."""
        self.turn = random.randint(1, 4)
        return self.turn

    def cycle(self) -> int:
        """Moving onto the next player."""
        return (self.turn + 1) % 4

    def next_round(self):
        """Reseting for the next round."""
        self.turn = self.initiate_turn()

    def bid(self):
        """Taking bid from the players."""
        for i in range(4):
            x = int(input(f"Enter the bid for player{i} = "))
            self.current_bid[i] = x

    def bid_count(self):
        """Storing the total achieved bids."""
        for i in range(4):
            if self.achieved_bid[i] < self.current_bid[i]:
                self.total_bid[i] -= self.current_bid[i]
            else:
                self.total_bid[i] = self.current_bid[i] + (self.achieved_bid - self.current_bid[i]) * 0.1

    def card_played(self):
        """Throwing the card."""
        self.throw = input("Throw the card : ")
        return self.throw
        # continue the code here

if __name__ == "__main__":
    r = Rules()
    r.higher_rank()

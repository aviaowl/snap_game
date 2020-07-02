from random import uniform
from time import time

from common.utils import colored
from src.cards import Card
from src.deck import Deck


class Player:
    """
    Class to represent a Player and simulate his actions.
    Player has two decks, one is for cards to play (hand) and another one is for discard cards or won cards (pile).

    Attributes:
        name (str): name of the player
        hand (Deck): cards in player's hands
        auto_mode (bool): if auto_mode is on, then count random latency for saying 'Snap!'
                          if auto_mode is off, wait for user's enter press and measure the latency
    Properties:
        pile (List[Card]): discard pile. In this list player stores won cards.
        has_card (bool):  flag indicates if player still has some cards in his hand
        pile_size (int): returns amount of won cards, need to determine which player has won the game
    Methods
        say_snap (auto_mode: bool = True) -
        turn () - extract card from player's deck and return it
    """

    def __init__(self, hand: Deck, name: str = None, auto_mode: bool = True):
        self.name = name
        self.hand = hand
        self.pile: Deck = Deck([])
        self.auto_mode = auto_mode

    def __repr__(self):
        return f"Player(name={self.name}, hand={self.hand})"

    @property
    def has_cards(self) -> bool:
        """True if player has cards in his hand"""
        return self.hand.size > 0

    @property
    def pile_size(self) -> int:
        """Return amount of won cards"""
        return self.pile.size

    def say_snap(self) -> float:
        """Returns the number of seconds for which the player said "SNAP".
        If the player is bot, generate a random dela.
        If the player is human, wait until he presses the enter button and count his delay in seconds"""
        if self.auto_mode:
            latency = round(uniform(0.50, 1.50), 2)
        else:
            time_before_say = time()
            input("Hurry! Press ENTER to say 'SNAP!'")
            time_after_say = time()
            latency = round(time_after_say - time_before_say, 2)
        print(
            f"{self.name} said {colored('SNAP!', 'YELLOW')} in {latency} seconds"
        )
        return latency

    def turn(self) -> Card:
        """Simulate player's turn. Take a card from player's hand, print message and return card"""
        taken_card = self.hand.get_card()
        print(
            f"Player {colored(self.name, 'BLUE')} "
            f"turned out {colored(str(taken_card), 'LIGHTBLUE_EX')}, hand size:",
            self.hand.size,
        )
        return taken_card

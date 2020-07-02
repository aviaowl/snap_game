from collections import deque
from typing import List

from src.cards import Card


class Deck:
    """Class for deck of cards representation

    Attributes:
        cards (List[Card]): list of playing cards in this deck
        size (int): amount of cards in the deck

    Methods:
        get_card: method for getting one card from the deck
        add_card: method for adding one new card to the deck
        fetch_all: method for fetching all cards of this deck to another one
    """

    def __init__(self, cards: List[Card]):
        self.deck = deque(list(cards))

    def __repr__(self):
        return ", ".join(str(card) for card in self.deck)

    def __iter__(self):
        for x in self.deck:
            yield x

    @property
    def size(self) -> int:
        """Returns amount of card in the deck"""
        return len(self.deck)

    def get_card(self):
        """Pop one card from the deck"""
        return self.deck.popleft()

    def add_card(self, card: Card):
        """Add one card to the deck"""
        self.deck.insert(0, card)

    def fetch_all(self, destination_deck):
        """Fetch all cards of this deck to another deck
        Args:
            destination_deck (Deck): deck to load all the cards
        Returns:
            Deck: Deck with extracted cards
        """
        while self.size:
            destination_deck.add_card(self.get_card())
        return destination_deck

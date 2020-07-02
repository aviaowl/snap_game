from dataclasses import dataclass


@dataclass(eq=False)
class Card:
    """Class to represent Card object
    Attributes:
        value (str): card's value (number/face). Should be in range [2, 10] or one of the following: J, Q, K, ACE
        suit (str): card's suite. Should be one of the following: SPADES, HEARTS, DIAMONDS, CLUBS
    """

    value: str
    suit: str

    def __eq__(self, other_card):
        """Method for cards comparison. Cards are equal if they have equal number/face"""
        if isinstance(other_card, Card):
            return self.value == other_card.value
        else:
            return False

    def __str__(self):
        """Method for string representation"""
        return f"{self.value} of {self.suit}"

    def __len__(self):
        return 1

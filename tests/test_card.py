import pytest

from src.cards import Card


@pytest.mark.parametrize(
    "value, suit",
    [
        ("2", "SPADES"),
        ("3", "HEARTS"),
        ("4", "DIAMONDS"),
        ("5", "CLUBS"),
        ("J", "SPADES"),
        ("Q", "HEARTS"),
        ("K", "DIAMONDS"),
        ("ACE", "CLUBS"),
    ],
)
def test_card_init(value: int, suit: str):
    """Test Card object initialization, all card numbers
    that greater than 10 should be converted to string"""
    card = Card(value=value, suit=suit)
    assert card.value == value
    assert card.suit == suit


@pytest.mark.parametrize(
    "first_card, second_card, expected",
    [
        (Card("3", "HEARTS"), Card("2", "DIAMONDS"), False),
        (Card("3", "SPADES"), Card("13", "HEARTS"), False),
        (Card("11", "HEARTS"), Card("12", "HEARTS"), False),
        (Card("3", "HEARTS"), Card("3", "DIAMONDS"), True),
        (Card("14", "SPADES"), Card("14", "CLUBS"), True),
        (Card("3", "HEARTS"), Card("3", "HEARTS"), True),
    ],
)
def test_card_comparison(first_card: Card, second_card: Card, expected: bool):
    """Test cards comparison: cards are True if their values are equal"""
    assert (first_card == second_card) == expected

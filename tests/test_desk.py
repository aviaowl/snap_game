from typing import List

import pytest

from src.cards import Card
from src.deck import Deck


@pytest.fixture
def cards() -> List[Card]:
    """Return list of cards"""
    return [
        Card(value=9, suit="DIAMONDS"),
        Card(value=9, suit="CLUBS"),
        Card(value=10, suit="SPADES"),
        Card(value="K", suit="DIAMONDS"),
        Card(value="ACE", suit="HEARTS"),
    ]


@pytest.fixture
def deck(cards) -> Deck:
    return Deck(cards)


def test_deck_get_card(deck):
    """Test getting a card from the deck and reaching deck's exhaustion"""
    assert str(deck.get_card()) == "9 of DIAMONDS"
    assert str(deck.get_card()) == "9 of CLUBS"
    assert str(deck.get_card()) == "10 of SPADES"
    assert str(deck.get_card()) == "K of DIAMONDS"
    assert str(deck.get_card()) == "ACE of HEARTS"
    assert deck.size == 0


def test_deck_add_card(deck):
    """Test card's addition"""
    assert deck.size == 5
    deck.add_card(Card(value="ACE", suit="CLUBS"))
    assert deck.size == 6
    assert deck.get_card() == Card(value="ACE", suit="CLUBS")


def test_deck_add_another_deck(deck, cards):
    """Test extracting all cards of one deck to another specified deck"""
    second_deck = Deck(
        (Card(value="ACE", suit="DIAMONDS"), Card(value="ACE", suit="SPADES"))
    )
    expected = list(deck) + list(second_deck)
    deck.fetch_all(second_deck)
    assert second_deck.size == 7
    assert not sum([not card in expected for card in second_deck])

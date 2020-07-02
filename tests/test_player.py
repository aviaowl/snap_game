from io import StringIO
from unittest.mock import patch

import pytest

from src.cards import Card
from src.deck import Deck
from src.player import Player


@pytest.fixture
def cards():
    return [
        Card(value=9, suit="DIAMONDS"),
        Card(value=9, suit="CLUBS"),
        Card(value=10, suit="SPADES"),
        Card(value="K", suit="DIAMONDS"),
        Card(value="ACE", suit="HEARTS"),
    ]


@pytest.fixture
def player(cards):
    return Player(name="Super Developer", hand=Deck(cards))


def test_player_init(player, cards):
    """Test default player init"""
    assert player.name == "Super Developer"
    assert isinstance(player.hand, Deck)
    assert isinstance(player.pile, Deck)
    assert list(player.hand) == cards
    assert list(player.pile) == []
    assert player.auto_mode is True
    assert player.has_cards is True
    assert player.pile_size == 0


@pytest.mark.parametrize("auto_mode", [True, False, None])
def test_player_say_snap(capsys, auto_mode: bool):
    """Check say_snap function, behaviour depends on auto_mode attribute"""
    player1 = Player(name="Witcher fan", hand=[], auto_mode=auto_mode)
    with patch("sys.stdin", StringIO("".join("I pressed Enter here"))):
        assert type(player1.say_snap()) is float
        # If auto_mode if False, expect waiting for input
        if not auto_mode:
            msg = capsys.readouterr()
            assert str(msg.out).startswith("Hurry! Press ENTER")


def test_player_turn(player, cards):
    """Check that method returns card from player's hand and hand's size is decreasing after that"""
    assert player.hand.size == len(cards)
    recieved_card = player.turn()
    assert isinstance(recieved_card, Card)
    assert recieved_card in cards
    assert player.hand.size == len(cards) - 1


def test_player_has_no_cards():
    """Check that is player has no cards, property returns False"""
    Daenerys = Player(
        name="Queen Daenerys Stormborn of the House Targaryen, the First of Her Name, "
        "Queen of the Andals, the Rhoynar and the First Men, "
        "Lady of the Seven Kingdoms and Protector of the Realm, "
        "Lady of Dragonstone, Queen of Meereen, "
        "Khaleesi of the Great Grass Sea, the Unburnt, Breaker of Chains and Mother of Dragons",
        hand=Deck([]),
    )
    assert not Daenerys.has_cards


def test_player_pile_size(player):
    """Check that pile size is changing after new cards addition"""
    assert player.pile_size == 0
    player.pile.add_card(Card(value="Q", suit="SPADES"))
    assert player.pile_size == 1

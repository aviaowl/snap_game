from itertools import product
from random import shuffle

from colorama import Fore, Style

from common.constants import *
from src.cards import Card


def get_input_data():
    players = input("[2] Enter amount of players for game: ")
    players = PLAYERS_DEFAULT if not players else players
    decks = input("[1] Enter amount of decks for game: ")
    decks = DECKS_AMOUNT if not decks else decks
    auto_mode = input("[0] Choose game mode: 0 - demo, 1 - game: ")
    auto_mode = True if not auto_mode or auto_mode == '0' else False
    name_player = input("[Optional] Enter your name: ")
    print("AUTO_MODE:", auto_mode)
    return dict(players_amount=int(players),
                decks_amount=int(decks),
                auto_mode=auto_mode,
                player_name=name_player)


def generate_deck(deck_number: int):
    all_cards = list(product(
        [i for i in range(2, 15)],
        CARD_SUITS)) * deck_number
    shuffle(all_cards)
    return [Card(*card) for card in all_cards]


def colored(msg, color):
    return getattr(Fore, color.upper()) + msg + Style.RESET_ALL

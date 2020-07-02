from random import shuffle
from time import sleep
from typing import List

from colorama import init

from common import utils
from common.constants import *
from common.utils import colored
from src.deck import Deck
from src.player import Player


def check_snap(desk_pile: Deck, players: List[Player]):
    """After every turn check if two last cards have the same value.
    If True, then every Player says 'SNAP' with his own latency is seconds.
    Round winner is the player with minimum latency, he takes all cards from the desk to his pile.
    Args:
        desk_pile (Deck): deck of cards that are currently at the table
        players (List[Player]): list of participating players
    """
    if desk_pile.size < 2:
        pass
    else:
        if list(desk_pile)[0] == list(desk_pile)[1]:
            latencies = []
            for player in players:
                latencies.append(player.say_snap())
            min_latency = latencies.index(min(latencies))
            round_winner: Player = list(players)[min_latency]
            print(
                f"{round_winner.name} won with {round(min(latencies), 2)} seconds latency "
                f"and grabbed {desk_pile.size} cards"
            )
            desk_pile.fetch_all(round_winner.pile)


def game(players: List[Player]):
    desk_pile = Deck([])
    turn_number = 1
    while players[0].has_cards:
        print("Turn", colored(f"{turn_number}", "YELLOW"))
        turn_number += 1
        for player in players:
            played_card = player.turn()
            desk_pile.add_card(played_card)
            check_snap(desk_pile, players)
        sleep(DEFAULT_TURN_TIME_SECONDS)
    pile_sizes = [player.pile_size for player in players]
    min_latency = pile_sizes.index(max(pile_sizes))
    game_winner: Player = list(players)[min_latency]
    print("############################")
    print(f"Player {utils.colored(game_winner.name, 'YELLOW')} WON!")
    print("############################")
    print(f"Game results:\n" + "\n".join(f"{player.name}: {player.pile_size} cards" for player in list(players)))


def chunk_deck(deck, size):
    return zip(*[iter(deck)] * size)


def prepare_game(decks_count, auto_mode, player_one_name, players_count):
    # define list of random names for bot-players
    random_names = RANDOM_NAMES
    shuffle(random_names)
    if player_one_name:
        names = [player_one_name] + random_names[: players_count - 1]
    else:
        names = random_names[:players_count]

    # generate cards and split all cards to the even chunks
    all_cards = utils.generate_deck(decks_count)
    chunked_deck = chunk_deck(all_cards, len(all_cards) // players_count)

    # initialize players
    players: List[Player] = []
    for player in zip(names, chunked_deck):
        players.append(Player(name=player[0], hand=Deck(player[1])))
    players[0].auto_mode = auto_mode
    return players


if __name__ == "__main__":
    init()
    # execute only if run as a script
    user_input: dict = utils.get_input_data()
    players = prepare_game(
        decks_count=user_input["decks_amount"],
        auto_mode=user_input["auto_mode"],
        player_one_name=user_input["player_name"],
        players_count=user_input["players_amount"],
    )
    game(players=players)

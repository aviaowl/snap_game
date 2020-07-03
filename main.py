from argparse import ArgumentParser, ArgumentTypeError
from itertools import product
from random import shuffle
from time import sleep
from typing import List

from src.constants import *
from src.cards import Card
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
    # if desk is empty, wait for new turns
    if desk_pile.size < 2:
        pass
    else:
        # compare two last card from the desk pile
        if list(desk_pile)[0] == list(desk_pile)[1]:
            latencies = []
            # every player is saying 'SNAP', save their latencies in seconds
            for player in players:
                latencies.append(player.say_snap())
            # determine round winner with minimal latency
            min_latency = latencies.index(min(latencies))
            round_winner: Player = list(players)[min_latency]
            print(
                f"{round_winner.name} won with {round(min(latencies), 2)} seconds latency "
                f"and grabbed {desk_pile.size} cards"
            )
            # round winner takes all cards from the desk pile to his own pile
            desk_pile.fetch_all(round_winner.pile)


def game(players: List[Player]):
    """Start the game with determined players.
    Steps:
        1. As long as the players have cards, each player takes turns placing the card on the table.
        2. After that, the snap is checked.
        3. When there are no cards left in our hands, find the winner of the game
            with the maximum number of cards in his pile.
    """
    desk_pile = Deck()
    turn_number = 0

    while players[0].has_cards:
        turn_number += 1
        print(f"Turn {turn_number}")
        for player in players:
            played_card = player.turn()
            desk_pile.add_card(played_card)
            check_snap(desk_pile, players)
        sleep(DEFAULT_TURN_TIME_SECONDS)

    pile_sizes = [(player, player.pile_size) for player in players]
    # sort from maximum player pile size to minimum, first player in the list wins the round
    pile_sizes.sort(key=lambda x: x[1], reverse=True)
    game_winner: Player = pile_sizes[0][0]

    # print game results
    print("############################")
    print(f"Player {game_winner.name} WON!")
    print("############################")
    print(
        f"Game results:\n"
        + "\n".join(
            f"{player.name}: {player.pile_size} cards" for player in list(players)
        )
    )


def chunk_deck(deck: Deck, size: int) -> List[List[Card]]:
    """Split all card to equal chunks
    Args:
        deck (Deck): all cards to split
        size (int): amount of necessary chunks
    Returns:
        List of card lists for every player
    """
    return zip(*[iter(deck)] * size)


def generate_deck(deck_number: int) -> List[Card]:
    """Method for generate requested amount of card decks
    Args:
        deck_number (int): requested amount of card
        """
    all_cards = list(product([i for i in range(2, 15)], CARD_SUITS)) * deck_number
    shuffle(all_cards)
    return [Card(*card) for card in all_cards]


def prepare_game(
    decks_count: int, auto_mode: bool, player_one_name: str, players_count: int
) -> List[Player]:
    """
    Initialize cards, decks, players for game
    Args:
        decks_count (int): amount of decks for the game
        auto_mode (bool): indicates if player one is bot or human
        player_one_name (str): name of player one. another names choose randomly
        players_count (int): amount of players for the game

    Returns:
        List[Player]: list of initialized players with cards
    """
    # define list of random names for bot-players
    random_names = RANDOM_NAMES
    shuffle(random_names)
    if player_one_name:
        names = [player_one_name] + random_names[: players_count - 1]
    else:
        names = random_names[:players_count]

    # generate cards and split all cards to the even chunks
    all_cards = generate_deck(decks_count)
    chunked_deck = chunk_deck(all_cards, len(all_cards) // players_count)

    # initialize players
    players: List[Player] = []
    for player, hand in zip(names, chunked_deck):
        players.append(Player(name=player, hand=Deck(hand)))
    # set auto_mode flag to the main player, because it's enabled by default
    players[0].auto_mode = auto_mode
    return players


def numeric_input(input_value: str) -> int:
    """Validate console arguments for players_amount and decks_amount
    Args:
        input_value (str) - string argument from the console
    Raises:
        ArgumentTypeError: if unable to convert string to integer or value not in range [1, 4]
    Returns:
        int: numeric argument from the console
    """
    try:
        input_value = int(input_value)
    except ValueError:
        pass
    if not isinstance(input_value, int):
        return ArgumentTypeError("Please specify number")
    if input_value < 1 or input_value > 4:
        return ArgumentTypeError("Value should be in range from 1 to 4")
    return input_value


def get_parser() -> ArgumentParser:
    """Parse console arguments
    Returns:
        Parsed arguments
    """
    parser = ArgumentParser()
    parser.add_argument(
        "--players",
        help="how many players will play, default 2",
        default=2,
        type=numeric_input,
    )
    parser.add_argument(
        "--decks",
        help="how many playing decks will be used, default 2",
        type=numeric_input,
        default=2,
    )
    parser.add_argument(
        "--auto_mode",
        help="if specified - demo mode, else game mode, default game_mode",
        action="store_true",
    )
    parser.add_argument(
        "--name_player",
        help="name of the main player, random name if not specified",
        type=str,
    )
    return parser


def main():
    """Get input, prepare and run game"""
    args = get_parser().parse_args()
    players = prepare_game(
        decks_count=args.decks,
        auto_mode=args.auto_mode,
        player_one_name=args.name_player,
        players_count=args.players,
    )
    game(players=players)


if __name__ == "__main__":
    main()

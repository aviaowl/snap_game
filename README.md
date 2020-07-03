# Snap game
Subscription manager is a tool that allows everyone to keep, track and analyze service subscriptions like Amazon Prime, Spotify, Coursera, etc in one place.

Tool has Telegram and command-line interfaces.

## How to play Snap
Snap! is a card game where all of the cards are shuffled and dealt equally to players (a group of 2, 3 or 4 people).

* Each player in turn turns over the top card from their face down dealt pile and puts it on top of their face up pile.

* When someone turns over a card that matches the value (same number, or same face) of a card on top of another player's face up pile, the players race to be the first to say “Snap!”
* The player who says “Snap!” first wins both piles and adds them to their winning pile.
* If more than one player says “Snap!” at the same time, the two piles are combined into the snap pot.
* Whoever wins the next snap wins the whole pot.
* At the end of the game, when all players have dealt their original hand of cards. The player with the most cards wins the game. 

## Application requirements
1. The task is to simulate a game of snap between two players using standard playing card decks.

2. The application should ask the user how many playing card decks to play with
3. The application should shuffle the decks before play commences
4. Games of snap should now be simulated. Cards are played one at a time and when two matching cards are dealt one after another the first player to shout snap wins. (You do not need to implement the case of a draw round)
The winner of each round collects all the cards dealt in this round
Once all cards in the deck are exhausted the application should declare the winner based on who has the most won cards

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.X

## Usage
Command-line interface:
```
usage: main.py [-h] [--players PLAYERS] [--decks DECKS] [--auto_mode]
               [--name_player NAME_PLAYER]

optional arguments:
  -h, --help            show this help message and exit
  --players PLAYERS     how many players will play, default 2
  --decks DECKS         how many playing decks will be used, default 2
  --auto_mode           if specified - demo mode, else game mode, default game_mode
  --name_player NAME_PLAYER
                        name of the main player, random name if not specified

```

## Contact

If you want to contact me you can reach me at [my email](mailto:romantsova.alina@gmail.com?subject=%5BGitHub%5D) or my [LinkedIn](https://www.linkedin.com/in/alina-romantsova-06ab06128/)

## License
This project is licensed under the terms of the MIT license.

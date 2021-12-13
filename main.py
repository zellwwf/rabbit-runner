import argparse
from game.game_manager import GameManager


def welcome_message():
    print("=====================================")
    print("==           Run Rabbit Run        ==")
    print("=====================================")


# Take in
# 1. N: the game size
# 2. M: Number of Games to Play
# 3. Strategies to run (add urs in the folder):
def setup_parser():
    parser = argparse.ArgumentParser(description="Run Rabbit!")
    parser.add_argument('-n', '--game-size', type=int, default=100, action="store")
    parser.add_argument('-m', '--max-turns', type=int, default=10000, action="store")
    parser.add_argument('-g', '--num-games', type=int, default=1, action="store")
    return parser


def main_entry():
    parser = setup_parser()
    welcome_message()
    args = vars(parser.parse_args())
    GameManager(args)
    GameManager.start_game()
    print("GAME ENDED ---")


if __name__ == "__main__":
    main_entry()

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()


def play_sweep(turn, game_size):
    return turn % (game_size - 1)


def play_stay_strategy():
    return 20


# We want to run G Games and terminate when the players submitted strategy found him
#
# Things we want to collect per game into a collection:
# 1. Turns it took to find the rabbit (current_turn when breaks)
# 2. Rabbit Locations array
# 3. Strategy Locations Array
# 4. TIME it took to find the rabbit.
class GameManager:
    """The class encapsulates the game data, run and stats"""
    max_turns = 100  # T
    game_size = 10  # N
    number_of_games = 10  # M
    rabbit_locations = None  # List of Lists (matrix)
    rabbit_histogram = None  # List of Lists (matrix)
    player_locations = None  # Matrix: n_cols = M, rows are moves per game (size of max turns, worst case)

    def __init__(self, params):
        self.game_size = params['game_size']
        self.max_turns = params['max_turns']
        self.number_of_games = params['num_games']

    def play_rabbit(self, location):
        if location == 0:
            rabbit_action = 1
        elif location == self.game_size - 1:
            rabbit_action = -1
        else:
            rabbit_action = rng.integers(low=0, high=2, size=1)
            rabbit_action = 2 * rabbit_action - 1

        location += rabbit_action
        return location

    def post_process_game_results(self, sweep_wins, stay_wins):
        print("Stay Wins", len(stay_wins), stay_wins[0])
        print("Sweep Wins", len(sweep_wins), sweep_wins[0])
        fig, (ax1, ax2) = plt.subplots(1, 2)

        print("Rabbit Started At Location: ", self.rabbit_locations[0])
        print("Rabbit Ended At Location: ", self.rabbit_locations[self.max_turns - 1])
        print("Histogram at stay location", self.rabbit_histogram[20])
        ax1.hist(self.rabbit_histogram)

        ax2.plot(self.rabbit_locations)
        print(self.rabbit_locations)
        plt.show()

    def start_game(self):
        # Setup data structures for post-processing and data collection.
        self.rabbit_histogram = np.zeros(self.game_size, dtype=np.uint16)
        self.rabbit_locations = np.zeros(self.max_turns, dtype=np.uint16)

        sweep_wins = []
        stay_wins = []

        # Play the First Turn.
        # Sets the rabbits starting location
        rabbit_location = rng.integers(self.game_size)
        self.rabbit_locations[0] = rabbit_location
        current_turn = 1

        # The Main Game Loop
        while current_turn < self.max_turns:
            # Move the game

            # The Rabbit Plays First. (Player 1)
            rabbit_location = self.play_rabbit(rabbit_location)

            # print(rabbit_location, rabbit_action)

            # The Player Plays Second (Player 2)
            sweep = play_sweep(current_turn, self.game_size)
            stay = play_stay_strategy()

            if sweep == rabbit_location:
                sweep_wins.append(['sweep', current_turn, rabbit_location])

            if stay == rabbit_location:
                stay_wins.append(['STAY', current_turn, rabbit_location])

            # Collect Data
            self.rabbit_locations[current_turn] = rabbit_location
            self.rabbit_histogram[rabbit_location] += 1

            # Next Turn!
            current_turn += 1

        # Plot & Post game processing
        self.post_process_game_results(sweep_wins, stay_wins)

        return

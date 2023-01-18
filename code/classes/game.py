"""
Solves rush hour with the given algorithm
"""

import pandas as pd
import matplotlib.pyplot as plt

class Game:
    def __init__(self, output_file, test_board, algorithm, \
        branch_and_bound = False, nr_moves_to_solve = None):

        self.output_file = output_file
        self.test_board = test_board
        self.algorithm = algorithm

        # keep track of all moves
        self.moves_df = pd.DataFrame(columns=['car name', 'move'])
        self.move_counter = 0

        # start solving with algorithm
        if branch_and_bound == True:
            self.nr_moves_to_solve = nr_moves_to_solve
            self.run_branch_and_bound()
        
        else:
            self.run()

    def run(self):
        pass


    def run_branch_and_bound(self):
        # keep moving cars until red car is at exit
        while self.win_check() == False and \
            self.move_counter < self.nr_moves_to_solve:
            self.move_counter += 1

            # make a move
            vehicle, direction = self.algorithm(self.test_board)

            # save movement
            self.append_move_to_DataFrame(vehicle, direction)

            # update the board with the new vehicle movement
            self.test_board.update_board()

            # plt.pause(0.005)

    def append_move_to_DataFrame(self, vehicle, direction):
        """
        Saves the move in a dataframe.
        """
        # append move to DataFrame
        move_df = pd.DataFrame([[vehicle.car, direction]], columns=['car name', 'move'])
        self.moves_df = pd.concat([self.moves_df, move_df])

    def win_check(self):
        """
        Checks whether the red car is positioned at the exit tile (=winning
        position). If so, end the game, print the number of moves needed to
        solve, create a csv file of the move dataframe and return True.
        Otherwise, return False.
        """
        if self.test_board.occupation[self.test_board.exit_tile] == self.test_board.red_car:
            self.nr_moves_to_solve = self.move_counter

            print(f"Rush Hour was solved in {self.nr_moves_to_solve} moves\n")
            self.output_maker()

            return True

        else:
            return False

    def output_maker(self):
        """
        Exports the dataframe of moves to a csv file.
        """
        self.moves_df.to_csv(self.output_file, index=False)
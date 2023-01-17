"""
Picks one random car movement of the given board and returns this movement.
"""

import random
import numpy as np
from ..classes import board

def random_car_move(test_board):
    """
    Picks a random vehicle to move.
    """
    # get all free squares
    free_row, free_col = test_board.get_free_squares()
    # pick random free square until vehicle moves
    pick_free_square = True

    while pick_free_square == True:
        # get the position of a randomly chosen free square
        free_row, free_col, r, c = random_free_square(free_row, free_col)

        # load_vehicles
        # list for random squares around free square
        surrounding_squares = ["left", "right", "up", "down"]

        # pick until all surroundings squares have been tried
        for _ in range(4):
            # choose a random surrounding square
            surr_square, surrounding_squares = random_surrounding_square(surrounding_squares)

            # move vehicle to the left respectively from free square
            if c + 1 < test_board.grid_size and \
            test_board.occupation[r][c + 1] >= 1 and surr_square == "left":
                neighbouring_veh = test_board.vehicle_dict[test_board.occupation[r][c + 1]]

                # only move if the orientation of the vehicle is horizontal
                if neighbouring_veh.orientation == "H":
                    test_board.move_vehicle_back(neighbouring_veh, r, c)

                    return neighbouring_veh, "left"

            # move vehicle to the right respectively from free square
            elif c - 1 >= 0 and \
            test_board.occupation[r][c - 1] >= 1 and surr_square == "right":
                neighbouring_veh = test_board.vehicle_dict[test_board.occupation[r][c - 1]]

                # only move if the orientation of the vehicle is horizontal
                if neighbouring_veh.orientation == "H":
                    test_board.move_vehicle_ahead(neighbouring_veh, r, c)

                    return neighbouring_veh, "right"

            # move vehicle to the up respectively from free square
            elif r + 1 < test_board.grid_size \
            and test_board.occupation[r + 1][c] >= 1 and surr_square == "up":
                neighbouring_veh = test_board.vehicle_dict[test_board.occupation[r + 1][c]]

                # only move if the orientation of the vehicle is vertical
                if neighbouring_veh.orientation == "V":
                    test_board.move_vehicle_back(neighbouring_veh, r, c)

                    return neighbouring_veh, "up"

            # move vehicle to the move respectively from free square
            elif r - 1 >= 0 and test_board.occupation[r - 1][c] >= 1 \
            and surr_square == "down":
                neighbouring_veh = test_board.vehicle_dict[test_board.occupation[r - 1][c]]

                # only move if the orientation of the vehicle is vertical
                if neighbouring_veh.orientation == "V":
                    test_board.move_vehicle_ahead(neighbouring_veh, r, c)

                    return neighbouring_veh, "down"

def random_free_square(row, col):
    """
    Picks a random free square and returns its position. Deletes it from the
    free square list to prevent it to not chose it again.
    """
    # pick random index for free square
    idx_square = random.randint(0, len(row) - 1)

    # get combination of row and col to determine position free square
    random_row = row[idx_square]
    random_col = col[idx_square]

    # delete chosen free square to not pick again
    row = np.delete(row, idx_square)
    col = np.delete(col, idx_square)

    return row, col, random_row, random_col

def random_surrounding_square(squares):
    """
    Chooses a random surrounding square from a list and returns this.
    """
    # pick random surrounding square
    surr_square = random.choice(squares)
    # delete from list to not pick again
    squares.remove(surr_square)

    return surr_square, squares

from ..classes import game
from ..classes import board

import numpy as np
import pandas as pd
import queue
import copy

# occupation_set = set()
# numberino = 0

def breath_first_search(start_state):
    moves_df = pd.DataFrame(columns=['car name', 'move'])
    child, children_parent_dict = search(start_state)
    print("test")
    # search back in dict to find all the moves made to get to winning state
    while children_parent_dict[child] != None:
        move, parent = children_parent_dict[child]
        child = parent

        # put move into df
        moves_df = append_move_to_DataFrame_reversed(moves_df, move)

    return moves_df


def search(start_state):
    # dictionary with children as key and as value a tuple of (move, parent)
    # where move is also a tuple of (vehicle, direction)
    children_parent_dict = {start_state: None}

    visited = set()
    q = queue.Queue()
    q.put(start_state)

    while not q.empty():
        current_state = q.get()
        # print(current_state.occupation)

        if current_state.occupation[current_state.exit_tile] \
        == current_state.red_car:
            print("winner winner chicken dinner")
        # game.Game.win_check(current_state) == True:
            return current_state, children_parent_dict

        if current_state in visited:
            continue

        visited.add(current_state)

        # print("next")
        next_states_list, children_parent_dict = get_next_states(current_state, children_parent_dict)
        print(f"number: {len(children_parent_dict)}")

        # children_parent_dict.update(child_dict)

        for next_state in next_states_list:
            q.put(next_state)

    return None



def get_next_states(current_state, children_parent_dict):
    next_states = []

    parent_state = copy.deepcopy(current_state)
    parent_occupation_tuple = str(tuple([tuple(row) for row in parent_state.occupation]))

    free_row, free_col = current_state.get_free_squares()

    direction_list = ["left", "right", "up", "down"]

    # systimatically go trough the empty tiles
    for free_tile_nbr in range(len(free_row)):

        r, c = free_row[free_tile_nbr], free_col[free_tile_nbr]

        for direction in direction_list:
            # make movement with the given surr_square
            vehicle = current_state.car_move(direction, r, c)

            if vehicle:
                # convert nparray to tuple of tuples
                current_occupation_tuple = str(tuple([tuple(row) for row in current_state.occupation]))

                if current_occupation_tuple not in children_parent_dict:
                    next_states.append(current_state)

                    children_parent_dict[current_occupation_tuple] = ((vehicle.car, direction), parent_occupation_tuple)
                    # print(current_state.occupation)
                    # numberino = numberino + 1
                    # occupation_set.add(current_occupation_tuple)
                    # print(occupation_set)
                    # print(f"number: {len(children_parent_dict)}")
                    # "reset" curent state
                    current_state = copy.deepcopy(parent_state)

    return next_states, children_parent_dict


def append_move_to_DataFrame_reversed(moves_df, move):
    # append move to DataFrame in reverse order since you start at the end
    move_df = pd.DataFrame([[move[0], move[1]]], columns=['car name', 'move'])
    moves_df = pd.concat([moves_df, move_df])

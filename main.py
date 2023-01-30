import argparse
import math
import copy
from tqdm import tqdm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from code.classes import board, game
from code.algorithms import randomise, randomise2, priority_red_car, breath_first

if __name__ == "__main__":
    # set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = 'solves rush hour')

    # adding arguments
    parser.add_argument("input_file", help = "location input file (csv)",)
    parser.add_argument("output_file", help = "location output file(csv)")

    # arguments for running experiments
    # parser.add_argument("output_png", help = "location output file(png)")
    # parser.add_argument("iterations", help = "the amount of runs you want done")

    # read arguments from command line
    args = parser.parse_args()

    # create a board for the data
    test_board = board.Board(f"data/gameboards/" + args.input_file)

    # -------- Test random algorithm to random with priority algorithm --------
    # random_moves_list = []
    # priority_moves_list = []
    #
    # for i in tqdm(range(int(args.iterations)), desc="Solving boards…", ascii=False, ncols=75):
    #     # run random algorithm
    #     test_game = game.Game(f"data/solutions/" + args.output_file, \
    #         copy.deepcopy(test_board), randomise.random_car_move)
    #
    #     # append the number of moves it took to solve the board to list
    #     number_of_moves_random = test_game.move_counter
    #     random_moves_list.append(number_of_moves_random)
    #
    #     # run random with priority algorithm
    #     test_game = game.Game(f"data/solutions/" + args.output_file, \
    #         copy.deepcopy(test_board), priority_red_car.move_priority_red_car)
    #
    #     # append the number of moves it took to solve the board to list
    #     number_of_moves_prio = test_game.move_counter
    #     priority_moves_list.append(number_of_moves_prio)
    #
    # # make lists into dataframe
    # moves_to_solve_df = pd.DataFrame({'total moves random': random_moves_list, \
    # 'total moves priority': priority_moves_list})
    #
    # # save dataframe to csv
    # moves_to_solve_df.to_csv(args.output_file, index=False)
    #
    # # plot data to histplot with kernal density estimate
    # sns.histplot(moves_to_solve_df, kde=True)
    # plt.xlabel('Total number of moves to reach winning state')
    # plt.xlim(0, 50000)
    # plt.ylim(0, 115)
    # plt.title('Arrangement of total number of moves needed to solve board 6x6_2')
    # plt.savefig(f"data/graphs/" + args.output_png)
    # plt.show()


    # # ----------- Solve by priority red car and random car movements -----------
    # moves_to_solve_priority_df = pd.DataFrame(columns=['total moves'])
    #
    # priority_list = []
    #
    # for i in tqdm(range(100), desc="Solving boards…", ascii=False, ncols=75):
    #     test_board = board.Board(f"data/gameboards/" + args.input_file)
    #     test_game = game.Game(f"data/solutions/" + args.output_file, \
    #             test_board, priority_red_car.move_priority_red_car)
    #
    #     number_of_moves = test_game.move_counter
    #     priority_list.append(number_of_moves)
    #
    # moves_to_solve_df['total moves priority'] = priority_list
    #
    #     # move_df = pd.DataFrame([number_of_moves], columns=['total moves'], index=[i])
    #     # moves_to_solve_priority_df = pd.concat([moves_to_solve_priority_df, move_df])
    #
    # moves_to_solve_df.to_csv(args.output_file, index=False)
    #
    # # sns.histplot(moves_to_solve_priority_df, stat='percent', ax=axis[1])
    # sns.histplot(moves_to_solve_df, stat='percent')
    #
    # plt.show()


    # ------------ Solve by random car movements - Branch and Bound ------------
    # nr_moves_to_solve = math.inf
    #
    # for i in tqdm(range(1), desc="Solving boards…", ascii=False, ncols=75):
    #     test_board = board.Board(f"data/gameboards/" + args.input_file)
    #     test_game = game.Game(f"data/solutions/" + args.output_file, \
    #         test_board, randomise.random_car_move, \
    #             branch_and_bound=True, nr_moves_to_solve=nr_moves_to_solve)
    #
    #     print(f"Rush Hour was solved in {test_game.nr_moves_to_solve} moves\n")
    #
    #     nr_moves_to_solve = test_game.nr_moves_to_solve


    # -- Solve by priority red car and random car movements - Branch and Bound--
    # nr_moves_to_solve = math.inf
    #
    # for i in tqdm(range(100000), desc="Solving boards…", ascii=False, ncols=75):
    #     test_board = board.Board(f"data/gameboards/" + args.input_file)
    #
    #     test_game = game.Game(f"data/solutions/" + args.output_file, \
    #             test_board, priority_red_car.move_priority_red_car, \
    #                 branch_and_bound=True, nr_moves_to_solve=nr_moves_to_solve)
    #
    #     nr_moves_to_solve = test_game.nr_moves_to_solve


    # -------------------- Solve by breath first algorithm ---------------------
    test_game = game.Game(f"data/solutions/" + args.output_file, \
        test_board, breath_first = True) #breath_first.breath_first_search,

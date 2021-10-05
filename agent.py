import random
import time

import numpy as np


class Agent:

    def __init__(self, name):
        self.id = name
        self.points = 0

    # make a random action based on the existing actions
    def random_action(self, env):
        possible_moves = env.available_moves()
        move = (())
        if env.player_turn == self.id:
            i = random.randint(0, len(possible_moves))
            move = (possible_moves[i][0], possible_moves[i][1])
            print(move, " by ", self.id)  # for debugging reasons
            env.move(move[0], move[1])

        return move

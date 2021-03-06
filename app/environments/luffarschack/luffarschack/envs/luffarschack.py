# Adapted from https://mblogscode.com/2016/06/03/python-naughts-crossestic-tac-toe-coding-unbeatable-ai/
<<<<<<< HEAD
import random
=======
>>>>>>> 8b953de (Added SIMPLE branch)

import gym
import numpy as np

import config

from stable_baselines import logger


class Player():
    def __init__(self, id, token):
        self.id = id
        self.token = token
        

class Token():
    def __init__(self, symbol, number):
        self.number = number
        self.symbol = symbol
        

    

class LuffarschackEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, verbose = False, manual = False):
        super(LuffarschackEnv, self).__init__()
        self.name = 'luffarschack'
        self.manual = manual
        
        self.grid_length = 9
        self.n_players = 2
        self.num_squares = self.grid_length * self.grid_length
        self.grid_shape = (self.grid_length, self.grid_length)
<<<<<<< HEAD
#        logger.debug('grid shape: ', self.grid_shape)
        self.action_space = gym.spaces.Discrete(self.num_squares)
        self.observation_space = gym.spaces.Box(-1, 1, self.grid_shape+(2,))
#        logger.debug('obs space: ', self.observation_space)
=======
        self.action_space = gym.spaces.Discrete(self.num_squares)
        self.observation_space = gym.spaces.Box(-1, 1, self.grid_shape+(2,))
>>>>>>> 8b953de (Added SIMPLE branch)
        self.verbose = verbose
        

    @property
    def observation(self):
        if self.players[self.current_player_num].token.number == 1:
            position = np.array([x.number for x in self.board]).reshape(self.grid_shape)
        else:
            position = np.array([-x.number for x in self.board]).reshape(self.grid_shape)

<<<<<<< HEAD
        #logger.debug('Position: ', position)
=======
>>>>>>> 8b953de (Added SIMPLE branch)
        la_grid = np.array(self.legal_actions).reshape(self.grid_shape)
        out = np.stack([position,la_grid], axis = -1)
        return out

    @property
    def legal_actions(self):
        legal_actions = []
        for action_num in range(len(self.board)):
            if self.board[action_num].number==0: #empty square
                legal_actions.append(1)
            else:
                legal_actions.append(0)
        return np.array(legal_actions)




    def square_is_player(self, square, player):
        return self.board[square].number == self.players[player].token.number

    def check_game_over(self):

        board = self.board
        current_player_num = self.current_player_num
        players = self.players


        # check game over
        # horizontals
        for i in range(self.grid_length):
            for j in range(self.grid_length - 4):
                if( self.square_is_player(i * self.grid_length + j, current_player_num) and
                    self.square_is_player(i * self.grid_length + j+1, current_player_num) and
                    self.square_is_player(i * self.grid_length + j+2, current_player_num) and
                    self.square_is_player(i * self.grid_length + j+3, current_player_num) and
                    self.square_is_player(i * self.grid_length + j+4, current_player_num) ):
                    return 1, True

        # verticals
        for i in range(self.grid_length - 4):
            for j in range(self.grid_length):
                if( self.square_is_player(i * self.grid_length + j, current_player_num) and
                    self.square_is_player((i+1) * self.grid_length + j, current_player_num) and
                    self.square_is_player((i+2) * self.grid_length + j, current_player_num) and
                    self.square_is_player((i+3) * self.grid_length + j, current_player_num) and
                    self.square_is_player((i+4) * self.grid_length + j, current_player_num) ):
                    return 1, True

        # diagonal /
        for i in range(4, self.grid_length):
<<<<<<< HEAD
            for j in range(4, self.grid_length):
                if( self.square_is_player((i-4) * self.grid_length + j, current_player_num) and
                    self.square_is_player((i-3) * self.grid_length + j-1, current_player_num) and
                    self.square_is_player((i-2) * self.grid_length + j-2, current_player_num) and
                    self.square_is_player((i-1) * self.grid_length + j-3, current_player_num) and
                    self.square_is_player(i * self.grid_length + j-4, current_player_num) ):
=======
            for j in range(self.grid_length - 4):
                if( self.square_is_player((i-4) * self.grid_length + j, current_player_num) and
                    self.square_is_player((i-3) * self.grid_length + j+1, current_player_num) and
                    self.square_is_player((i-2) * self.grid_length + j+2, current_player_num) and
                    self.square_is_player((i-1) * self.grid_length + j+3, current_player_num) and
                    self.square_is_player(i * self.grid_length + j+4, current_player_num) ):
>>>>>>> 8b953de (Added SIMPLE branch)
                    return 1, True

        # diagonal \
        for i in range(self.grid_length - 4):
            for j in range(self.grid_length - 4):
                if (self.square_is_player(i * self.grid_length + j, current_player_num) and
                        self.square_is_player((i+1) * self.grid_length + j + 1, current_player_num) and
                        self.square_is_player((i+2) * self.grid_length + j + 2, current_player_num) and
                        self.square_is_player((i+3) * self.grid_length + j + 3, current_player_num) and
                        self.square_is_player((i+4) * self.grid_length + j + 4, current_player_num)):
                    return 1, True

        if self.turns_taken == self.num_squares:
            logger.debug("Board full")
            return 0, True

        return 0, False

    @property
    def current_player(self):
        return self.players[self.current_player_num]


    def step(self, action):
        
        reward = [0, 0]
        
        # check move legality
        board = self.board
        
        if (board[action].number != 0):  # not empty
            done = True
            reward = [1, 1]
            reward[self.current_player_num] = -1
        else:
            board[action] = self.current_player.token
            self.turns_taken += 1
            r, done = self.check_game_over()
            reward = [-r*2, -r*2]
            reward[self.current_player_num] = r

        self.done = done

        if not done:

            friends_in_area = self.check_surroundings(3, self.current_player_num, action)
#            enemies_adjacent = self.check_surroundings(1, (self.current_player_num + 1) % 2, action)
#            friends_adjacent = self.check_surroundings(1, self.current_player_num, action)
    
            reward[self.current_player_num] += 0.001 * friends_in_area
#            reward[self.current_player_num] += 0.02 * enemies_adjacent
#            reward[self.current_player_num] += 0.03 * friends_adjacent
            reward[self.current_player_num] += 0.01 * (self.in_a_row(action)-1)
            reward[self.current_player_num] += 0.01 * (self.in_a_col(action)-1)
            reward[self.current_player_num] += 0.01 * (self.in_a_diagonal(action)-1)
            reward[self.current_player_num] += 0.01 * (self.in_an_other_diagonal(action)-1)

    
            if not self.turns_taken == 1 and not friends_in_area: # and not enemies_adjacent:
                reward[self.current_player_num] -= 0.02

            logger.debug("Rewards: ", reward)
            
            self.current_player_num = (self.current_player_num + 1) % 2

        return self.observation, reward, done, {}

    def check_surroundings(self, search_rad, player_num, action):
        x0 = action % self.grid_length
        y0 = action // self.grid_length
        
        counter = 0
        for i in range(self.grid_length):
            for j in range(self.grid_length):
                if self.square_is_player(i * self.grid_length + j, player_num):
                    if 0 < abs(x0 - j) + abs(y0 - i) <= search_rad:
                        counter += 1
    
        return counter


#   check on the same row -> loop over columns
    def in_a_row(self, action):
        #columns
        x0 = action % self.grid_length
        #rows
        y0 = action // self.grid_length

        counter = 0
        passed_x0 = False

        for i in range(x0-4, x0+5):
            if not i // self.grid_length == x0 // self.grid_length:
                continue

            if i > x0:
                passed_x0 = True

            if self.square_is_player(y0*self.grid_length + i, self.current_player_num):
                counter += 1
            elif passed_x0:
                break
            else:
                counter = 0

        return counter

    def in_a_col(self, action):
        #columns
        x0 = action % self.grid_length
        #rows
        y0 = action // self.grid_length

        counter = 0
        passed_y0 = False

        for i in range(y0-4, y0+5):
            if i < 0:
                continue
            if i > 8:
                break

            if i > y0:
                passed_y0 = True

            if self.square_is_player(i*self.grid_length + x0, self.current_player_num):
                counter += 1
            elif passed_y0:
                break
            else:
                counter = 0

        return counter

# diagonal \
    def in_a_diagonal(self, action):
        #columns
        x0 = action % self.grid_length
        #rows
        y0 = action // self.grid_length

        counter = 0
        passed_action = False

        for i in range(-4, 5):
            if (x0 + i) >= self.grid_length or (y0 + i) >= self.grid_length:
                break
            if (x0 + i) < 0 or (y0 + i) < 0:
                continue

            if i > 0:
                passed_action = True

            if self.square_is_player((y0 + i) * self.grid_length + x0 + i, self.current_player_num):
                counter += 1
            elif passed_action:
                break
            else:
                counter = 0

        return counter

# diagonal /
    def in_an_other_diagonal(self, action):
        # columns
        x0 = action % self.grid_length
        # rows
        y0 = action // self.grid_length

        counter = 0
        passed_action = False

        for i in range(-4, 5):
            if (x0 - i) >= self.grid_length or (y0 + i) < 0:
                continue
            if (x0 - i) < 0 or (y0 + i) >= self.grid_length:
                break

            if i > 0:
                passed_action = True

            if self.square_is_player((y0 + i) * self.grid_length + x0 - i, self.current_player_num):
                counter += 1
            elif passed_action:
                break
            else:
                counter = 0

        return counter

    def reset(self):
        self.board = [Token('.', 0)] * self.num_squares
        self.players = [Player('1', Token('X', 1)), Player('2', Token('O', -1))]
        self.current_player_num = 0
        self.turns_taken = 0
        self.done = False
        logger.debug(f'\n\n---- NEW GAME ----')
        return self.observation


    def render(self, mode='human', close=False, verbose = True):
<<<<<<< HEAD

=======
        logger.debug('')
>>>>>>> 8b953de (Added SIMPLE branch)
        if close:
            return
        if self.done:
            logger.debug(f'GAME OVER')
        else:
            logger.debug(f"It is Player {self.current_player.id}'s turn to move")
<<<<<<< HEAD

        for i in range(self.grid_length):
            logger.debug(' '.join([x.symbol for x in self.board[i*self.grid_length:self.grid_length*(i+1)]]))

<<<<<<< HEAD
        # logger.debug(' '.join([x.symbol for x in self.board[:self.grid_length]]))
        # logger.debug(' '.join([x.symbol for x in self.board[self.grid_length:self.grid_length*2]]))
        # logger.debug(' '.join([x.symbol for x in self.board[(self.grid_length*2):(self.grid_length*3)]]))
=======
            
        logger.debug(' '.join([x.symbol for x in self.board[:self.grid_length]]))
        logger.debug(' '.join([x.symbol for x in self.board[self.grid_length:self.grid_length*2]]))
        logger.debug(' '.join([x.symbol for x in self.board[(self.grid_length*2):(self.grid_length*3)]]))
>>>>>>> 8b953de (Added SIMPLE branch)

=======
>>>>>>> 66e5843 (Changed board to 9by9 and modified rewards)
        if self.verbose:
            logger.debug(f'\nObservation: \n{self.observation}')
        
        if not self.done:
            logger.debug(f'\nLegal actions: {[i for i,o in enumerate(self.legal_actions) if o != 0]}')


    def rules_move(self):
        if self.current_player.token.number == 1:
            b = [x.number for x in self.board]
        else:
            b = [-x.number for x in self.board]

<<<<<<< HEAD
        #logger.debug('b: ', b)

        return self.create_action_probs(random.randint(0, 80))


        # Check computer win moves
        # for i in range(0, self.num_squares):
        #     if b[i] == 0 and testWinMove(b, 1, i):
        #         logger.debug('Winning move')
        #         return self.create_action_probs(i)
        # # Check player win moves
        # for i in range(0, self.num_squares):
        #     if b[i] == 0 and testWinMove(b, -1, i):
        #         logger.debug('Block move')
        #         return self.create_action_probs(i)
        # # Check computer fork opportunities
        # for i in range(0, self.num_squares):
        #     if b[i] == 0 and testForkMove(b, 1, i):
        #         logger.debug('Create Fork')
        #         return self.create_action_probs(i)
        # # Check player fork opportunities, incl. two forks
        # playerForks = 0
        # for i in range(0, self.num_squares):
        #     if b[i] == 0 and testForkMove(b, -1, i):
        #         playerForks += 1
        #         tempMove = i
        # if playerForks == 1:
        #     logger.debug('Block One Fork')
        #     return self.create_action_probs(tempMove)
        # elif playerForks == 2:
        #     for j in [1, 3, 5, 7]:
        #         if b[j] == 0:
        #             logger.debug('Block 2 Forks')
        #             return self.create_action_probs(j)
        #
        # # Play center
        # if b[4] == 0:
        #     logger.debug('Play Centre')
        #     return self.create_action_probs(4)
        # # Play a corner
        # for i in [0, 2, 6, 8]:
        #     if b[i] == 0:
        #         logger.debug('Play Corner')
        #         return self.create_action_probs(i)
        # #Play a side
        # for i in [1, 3, 5, 7]:
        #     if b[i] == 0:
        #         logger.debug('Play Side')
        #         return self.create_action_probs(i)


    def create_action_probs(self, action):
        #logger.debug('Action: ', action)
        action_probs = [0.001] * self.action_space.n
        action_probs[action] = 0.64
        return action_probs
=======
        # Check computer win moves
        for i in range(0, self.num_squares):
            if b[i] == 0 and testWinMove(b, 1, i):
                logger.debug('Winning move')
                return self.create_action_probs(i)
        # Check player win moves
        for i in range(0, self.num_squares):
            if b[i] == 0 and testWinMove(b, -1, i):
                logger.debug('Block move')
                return self.create_action_probs(i)
        # Check computer fork opportunities
        for i in range(0, self.num_squares):
            if b[i] == 0 and testForkMove(b, 1, i):
                logger.debug('Create Fork')
                return self.create_action_probs(i)
        # Check player fork opportunities, incl. two forks
        playerForks = 0
        for i in range(0, self.num_squares):
            if b[i] == 0 and testForkMove(b, -1, i):
                playerForks += 1
                tempMove = i
        if playerForks == 1:
            logger.debug('Block One Fork')
            return self.create_action_probs(tempMove)
        elif playerForks == 2:
            for j in [1, 3, 5, 7]:
                if b[j] == 0:
                    logger.debug('Block 2 Forks')
                    return self.create_action_probs(j)
        # Play center
        if b[4] == 0:
            logger.debug('Play Centre')
            return self.create_action_probs(4)
        # Play a corner
        for i in [0, 2, 6, 8]:
            if b[i] == 0:
                logger.debug('Play Corner')
                return self.create_action_probs(i)
        #Play a side
        for i in [1, 3, 5, 7]:
            if b[i] == 0:
                logger.debug('Play Side')
                return self.create_action_probs(i)


    def create_action_probs(self, action):
        action_probs = [0.01] * self.action_space.n
        action_probs[action] = 0.92
        return action_probs   
>>>>>>> 8b953de (Added SIMPLE branch)


def checkWin(b, m):
    return ((b[0] == m and b[1] == m and b[2] == m) or  # H top
            (b[3] == m and b[4] == m and b[5] == m) or  # H mid
            (b[6] == m and b[7] == m and b[8] == m) or  # H bot
            (b[0] == m and b[3] == m and b[6] == m) or  # V left
            (b[1] == m and b[4] == m and b[7] == m) or  # V centre
            (b[2] == m and b[5] == m and b[8] == m) or  # V right
            (b[0] == m and b[4] == m and b[8] == m) or  # LR diag
            (b[2] == m and b[4] == m and b[6] == m))  # RL diag


<<<<<<< HEAD
# def checkDraw(b):
#     return 0 not in b
#
# def getBoardCopy(b):
#     # Make a duplicate of the board. When testing moves we don't want to
#     # change the actual board
#     dupeBoard = []
#     for j in b:
#         dupeBoard.append(j)
#     return dupeBoard
#
# def testWinMove(b, mark, i):
#     # b = the board
#     # mark = 0 or X
#     # i = the square to check if makes a win
#     bCopy = getBoardCopy(b)
#     bCopy[i] = mark
#     return checkWin(bCopy, mark)
#
#
# def testForkMove(b, mark, i):
#     # Determines if a move opens up a fork
#     bCopy = getBoardCopy(b)
#     bCopy[i] = mark
#     winningMoves = 0
#     for j in range(0, 9):
#         if testWinMove(bCopy, mark, j) and bCopy[j] == 0:
#             winningMoves += 1
#     return winningMoves >= 2
=======
def checkDraw(b):
    return 0 not in b

def getBoardCopy(b):
    # Make a duplicate of the board. When testing moves we don't want to 
    # change the actual board
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard

def testWinMove(b, mark, i):
    # b = the board
    # mark = 0 or X
    # i = the square to check if makes a win 
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    return checkWin(bCopy, mark)


def testForkMove(b, mark, i):
    # Determines if a move opens up a fork
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    winningMoves = 0
    for j in range(0, 9):
        if testWinMove(bCopy, mark, j) and bCopy[j] == 0:
            winningMoves += 1
    return winningMoves >= 2
>>>>>>> 8b953de (Added SIMPLE branch)

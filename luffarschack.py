import numpy as np


class Player:
    def __init__(self, _id):
        self.id = _id


class Game:
    def __init__(self):
        self.board_size = 19
        self.n_players = 2
        self.board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.player_turn = -1  # Changes every move

        
    def move(self, row, col):
        if self.legal_move(row, col):
            self.board[row][col] = self.player_turn
            self.player_turn *= -1
            return True

        return False
    
    def legal_move(self, row, col) -> bool:
        # Checks so move is within board boundary
        if -1 < row < self.board_size and -1 < col < self.board_size:
            return self.board[row][col] == 0

        return False

    
    def check_game_over(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                # Checks vertical
                if col < self.board_size - 4 and \
                        abs(self.board[row][col] +
                       self.board[row][col+1] +
                       self.board[row][col+2] +
                       self.board[row][col+3] +
                       self.board[row][col+4]) == 5:
                    return self.board[row][col], True
                
                # Checks horizontal
                if row < self.board_size - 4 and \
                        abs(self.board[row][col] +
                       self.board[row+1][col] +
                       self.board[row+2][col] +
                       self.board[row+3][col] +
                       self.board[row+4][col]) == 5:
                    return self.board[row][col], True
                
                # Checks \ diagonal
                if row < self.board_size - 4 and \
                    col < self.board_size - 4 and \
                        abs(self.board[row][col] +
                       self.board[row+1][col+1] +
                       self.board[row+2][col+2] +
                       self.board[row+3][col+3] +
                       self.board[row+4][col+4]) == 5:
                    return self.board[row][col], True
                
                # Checks / diagonal
                if row < self.board_size - 4 and \
                    col > 3 and \
                    abs(self.board[row][col] +
                       self.board[row+1][col-1] +
                       self.board[row+2][col-2] +
                       self.board[row+3][col-3] +
                       self.board[row+4][col-4]) == 5:
                    return self.board[row][col], True

        # Checks if tie
        if 0 in self.board:
            return 0, False
        else:
            return 0, True


    def clear_board(self):
        self.board.fill(0)
        self.player_turn = -1

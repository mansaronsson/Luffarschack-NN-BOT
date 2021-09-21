import numpy as np


class Player:
    def __init__(self):
        self.id = 0


class Game:
    def __init__(self):
        self.board_size = 19
        self.board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.player_turn = -1  # Changes every move
    
    def print_state(self):
        print(self.board)
        
    def move(self, row, col):
        if self.legal_move(row, col):
            self.board[row][col] = self.player_turn
            self.player_turn *= -1
    
    def legal_move(self, row, col) -> bool:
        return self.board[row][col] == 0
    
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
                    return self.board[row][col]
                
                # Checks horizontal
                elif row < self.board_size - 4 and \
                        abs(self.board[row][col] +
                       self.board[row+1][col] +
                       self.board[row+2][col] +
                       self.board[row+3][col] +
                       self.board[row+4][col]) == 5:
                    return self.board[row][col]
                
                # Checks \ diagonal
                elif row < self.board_size - 4 and \
                    col < self.board_size - 4 and \
                        abs(self.board[row][col] +
                       self.board[row+1][col+1] +
                       self.board[row+2][col+2] +
                       self.board[row+3][col+3] +
                       self.board[row+4][col+4]) == 5:
                    return self.board[row][col]
                
                # Checks / diagonal
                elif row < self.board_size - 4 and \
                    col > 4 and \
                    abs(self.board[row][col] +
                       self.board[row+1][col-1] +
                       self.board[row+2][col-2] +
                       self.board[row+3][col-3] +
                       self.board[row+4][col-4]) == 5:
                    return self.board[row][col]
        return 0

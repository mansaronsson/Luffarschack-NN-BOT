import numpy as np


class Player:
    def __init__(self, _id):
        self.id = _id


class Game:
    def __init__(self, p1, p2):
        self.board_size = 19
        self.n_players = 2
        self.player1 = p1
        self.player2 = p2
        self.board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.player_turn = self.player1.id  # Changes every move
        self.last_turn = self.player1

    def move(self, row, col):
        if self.legal_move(row, col):
            self.board[row][col] = self.player_turn
            self.last_turn = self.board[row][col]
            self.player_turn = self.player1.id if (self.player_turn == self.player2.id) else self.player2.id
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

    def check_win(self, move):
        numbers_in_row = 0
        numbers_in_col = 0
        numbers_in_diagonal_ud = 0
        numbers_in_diagonal_du = 0

# check row of placement
        for row in range(self.board_size):
            if self.board[row][move[1]] == self.last_turn:
                numbers_in_row += 1
                if numbers_in_row == 5:
                    return self.last_turn, True
            else:
                numbers_in_row = 0

# check col of placement
        for col in range(self.board_size):
            if self.board[move[0]][col] == self.last_turn:
                numbers_in_col += 1
                if numbers_in_col == 5:
                    return self.last_turn, True
            else:
                numbers_in_col = 0


# diagonal of placement top left to bottom right

        for i in range(-4, 4):
            if move[0]+i < 0 or move[1]+i < 0:
                continue
            elif (move[0] + i) == self.board_size or (move[1] + i) == self.board_size:
                break

            if self.board[move[0]+i][move[1]+i] == self.last_turn:
                numbers_in_diagonal_ud += 1
                if numbers_in_diagonal_ud == 5:
                    return self.last_turn, True
            else:
                numbers_in_diagonal_ud = 0

# diagonal low right to top left
        for i in range(-4, 4):
            print(move[0]-i, " and ", move[1]+i)
            if move[0]-i < 0 or move[1]+i < 0:
                continue
            if move[0]-i >= self.board_size or move[1]+i >= self.board_size:
                continue

            if self.board[move[0]-i][move[1]+i] == self.last_turn:
                numbers_in_diagonal_du += 1
                if numbers_in_diagonal_du == 5:
                    return self.last_turn, True
            else:
                numbers_in_diagonal_du = 0

        return 0, False

# diagonal right to left

#       for col in range(self.board_size):
#          if self.board[col][col] == self.last_turn:
#             numbers_in_row += 1
#        else:
#           numbers_in_row = 0
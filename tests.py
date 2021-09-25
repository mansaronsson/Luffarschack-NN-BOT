from luffarschack import *


def run_tests():

    test = Game()

    # Left upper diagonal test
    test.move(0, 0)
    test.move(5, 5)
    test.move(1, 1)
    test.move(5, 7)
    test.move(2, 2)
    test.move(9, 9)
    test.move(3, 3)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(4, 4)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Right lower diagonal test
    test.move(18, 18)
    test.move(5, 5)
    test.move(17, 17)
    test.move(5, 7)
    test.move(16, 16)
    test.move(9, 9)
    test.move(15, 15)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(14, 14)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Right upper diagonal test
    test.move(0, 18)
    test.move(5, 5)
    test.move(1, 17)
    test.move(5, 7)
    test.move(2, 16)
    test.move(9, 9)
    test.move(3, 15)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(4, 14)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Right upper diagonal test
    test.move(18, 0)
    test.move(5, 5)
    test.move(17, 1)
    test.move(5, 7)
    test.move(16, 2)
    test.move(9, 9)
    test.move(15, 3)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(14, 4)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Left upper horizontal test
    test.move(0, 0)
    test.move(5, 5)
    test.move(0, 1)
    test.move(5, 7)
    test.move(0, 2)
    test.move(9, 9)
    test.move(0, 3)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(0, 4)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Left upper vertical test
    test.move(0, 0)
    test.move(5, 5)
    test.move(1, 0)
    test.move(5, 7)
    test.move(2, 0)
    test.move(9, 9)
    test.move(3, 0)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(4, 0)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Right upper horizontal test
    test.move(0, 18)
    test.move(5, 5)
    test.move(0, 17)
    test.move(5, 7)
    test.move(0, 16)
    test.move(9, 9)
    test.move(0, 15)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(0, 14)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Right upper vertical test
    test.move(0, 18)
    test.move(5, 5)
    test.move(1, 18)
    test.move(5, 7)
    test.move(2, 18)
    test.move(9, 9)
    test.move(3, 18)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(4, 18)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Left lower horizontal test
    test.move(18, 0)
    test.move(5, 5)
    test.move(18, 1)
    test.move(5, 7)
    test.move(18, 2)
    test.move(9, 9)
    test.move(18, 3)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(18, 4)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Left lower vertical test
    test.move(18, 0)
    test.move(5, 5)
    test.move(17, 0)
    test.move(5, 7)
    test.move(16, 0)
    test.move(9, 9)
    test.move(15, 0)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(14, 0)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Right lower horizontal test
    test.move(18, 18)
    test.move(5, 5)
    test.move(18, 17)
    test.move(5, 7)
    test.move(18, 16)
    test.move(9, 9)
    test.move(18, 15)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(18, 14)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Right lower vertical test
    test.move(18, 18)
    test.move(5, 5)
    test.move(17, 18)
    test.move(5, 7)
    test.move(16, 18)
    test.move(9, 9)
    test.move(15, 18)
    test.move(2, 9)
    # print(test.board)
    assert not test.check_game_over()[1]
    test.move(14, 18)
    # print(test.board)
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == -1
    test.clear_board()

    # Checks if tie
    test.board.fill(2)
    test.board[0][0] = 0
    assert not test.check_game_over()[1]
    test.board[0][0] = 2
    assert test.check_game_over()[1]
    assert test.check_game_over()[0] == 0

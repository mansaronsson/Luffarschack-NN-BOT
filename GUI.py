import PySimpleGUI as sg
from luffarschack import *


class GUI:
    def __init__(self, game):

        board = [[0 for j in range(game.board_size)] for i in range(game.board_size)]

        layout = [[sg.Button('', size=(4, 2), key=(i, j), pad=(0, 0)) for j in range(game.board_size)] for i in
                  range(game.board_size)]

        window = sg.Window('Luffarschack', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            # window[(row, col)].update('New text')   # To change a button's text, use this pattern
            # For this example, change the text of the button to the board's value and turn color black
            window[event].update(board[event[0]][event[1]], button_color=('white', 'black'))
        window.close()

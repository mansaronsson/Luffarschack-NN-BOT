import random

import PySimpleGUI as sg
import time
from luffarschack import *


class GUI:
    def __init__(self, game):

        board = game.board

        layout = [[sg.Button('', size=(4, 2), key=(i, j), pad=(0, 0)) for j in range(game.board_size)] for i in
                  range(game.board_size)]

        window = sg.Window('Luffarschack', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            # i = event[0] and j = event[j]

            if game.legal_move(event[0], event[1]):
                window[event].update(game.player_turn, button_color=('white', 'black'))
            game.move(event[0], event[1])

            print(game.available_moves())

            if game.check_win(event)[1]:
                print("we have a winner", game.check_win(event)[0])
                break

        window.close()

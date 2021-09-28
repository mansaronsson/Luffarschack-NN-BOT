from luffarschack import *
from GUI import *
import tests


def main():

    # Our tests in tests.py
    #tests.run_tests()
    p1 = Player(1)
    p2 = Player(2)
    game = Game(p1, p2)
    gui = GUI(game)


# Runs main when running file
if __name__ == "__main__":
    main()

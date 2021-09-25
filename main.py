from luffarschack import *
from GUI import *
import tests


def main():

    # Our tests in tests.py
    tests.run_tests()

    game = Game()
    gui = GUI(game)


# Runs main when running file
if __name__ == "__main__":
    main()

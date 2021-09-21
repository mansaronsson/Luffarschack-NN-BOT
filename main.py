from luffarschack import *


def main():

    test = Game()
    test.print_state()
    test.move(0, 0)
    test.move(5, 5)
    test.move(0, 1)
    test.move(5, 7)
    test.move(0, 2)
    test.move(9, 9)
    test.move(0, 3)
    test.move(2, 9)
    
    print(test.check_game_over())
    test.print_state()
    test.move(0, 4)
    test.print_state()
    print(test.check_game_over())
    

# Runs main when running file
if __name__ == "__main__":
    main()

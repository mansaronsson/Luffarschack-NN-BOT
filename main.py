from luffarschack import *
from agent import *
from GUI import *
import tests


def main():

    # Our tests in tests.py
    #tests.run_tests()
    p1 = Player(1)
    p2 = Player(2)

    agent1 = Agent(1)
    agent2 = Agent(2)

# with a gui, does not work for "AI"
#    game = Game(p1, p2)
#    gui = GUI(game)

    game_w_agents = Game(agent1, agent2)
    print(game_w_agents.player1.id)
    print(game_w_agents.player2.id)

    while True:
        possible_moves = game_w_agents.available_moves()
        if len(possible_moves) == 0:
            print("no more available moves")
            break

#        time.sleep(0.5)
        latest_move = (())
        if game_w_agents.player_turn == agent1.id:
            latest_move = agent1.random_action(game_w_agents)
        elif game_w_agents.player_turn == agent2.id:
            latest_move = agent2.random_action(game_w_agents)

        if game_w_agents.check_win(latest_move)[1]:
            print("we have a winner = ", game_w_agents.check_win(latest_move)[0])
            break

# old code now implemented in the agents
#        i = random.randint(0, len(possible_moves))
#        move = (possible_moves[i][0], possible_moves[i][1])
#        game_w_agents.move(move[0], move[1])
#        print(move, " made by ", game_w_agents.last_turn)

#        if game_w_agents.check_win(move)[1]:
#            print("we have a winner = ", game_w_agents.check_win(move)[0])
#            break


# Runs main when running file
if __name__ == "__main__":
    main()

from ast import literal_eval

import consts
from game import Game
from snake import Snake


def init_game() -> Game:
    board_size = max(int(input()), consts.MINIMUM_BOARD_SIZE)

    num_moves = int(input())
    foods = [food for food in literal_eval(input()) if board_size > food[0] >= 0 and board_size > food[1] >= 0]
    snake = Snake(board_size)

    return Game(board_size, num_moves, foods, snake, input)


def main():
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        print(case)
        game = init_game()
        game.run()
        total_length = game.snake_length
        print("Case #{}: {}".format(case, total_length))


if __name__ == '__main__':
    main()

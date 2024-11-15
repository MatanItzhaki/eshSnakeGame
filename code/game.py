from itertools import cycle
from typing import Callable

import consts
from snake import Snake


class Game:
    def __init__(self, board_size: int, num_moves: int, foods: list,
                 snake: Snake, input_supplier: Callable[[], str]) -> None:
        self.__board_size = board_size
        self.__num_moves = num_moves
        self.__foods = cycle(foods)
        self.__foods_count = len(foods)
        self.__snake = snake
        self.__input_supplier = input_supplier
        self.__continue_playing = True
        self.__next_food()

    @property
    def snake_length(self):
        return self.__snake.length

    def run(self) -> None:
        for _ in range(self.__num_moves):
            move_key = self.__input_supplier()

            if not self.__continue_playing:
                continue

            if move_key == consts.PAUSE_KEY:
                self.__pause()

            if move_key in consts.KEYPAD.keys():
                move_direction = consts.KEYPAD[move_key]
            else:
                move_direction = self.__snake.direction

            if self.__current_food is None:
                self.__snake.move(move_direction)
                self.__next_food()
            elif self.__snake.can_eat(move_direction, self.__current_food):
                self.__snake.eat(move_direction)
                self.__next_food()
            else:
                self.__snake.move(move_direction)

            self.__continue_playing = not self.__game_over()

    def __pause(self) -> None:
        pause_key = self.__input_supplier()
        while pause_key == consts.PAUSE_KEY:
            pause_key = self.__input_supplier()

    def __next_food(self) -> None:
        snake_positions = self.__snake.positions
        for _ in range(self.__foods_count):
            self.__current_food = next(self.__foods)
            if self.__current_food not in snake_positions:
                return

        self.__current_food = None

    def __game_over(self) -> bool:
        snake_head = self.__snake.head
        if snake_head[0] < 0 or snake_head[0] >= self.__board_size \
                or snake_head[1] < 0 or snake_head[1] >= self.__board_size:
            return True

        snake_positions = self.__snake.positions
        snake_positions.popleft()

        return snake_head in snake_positions

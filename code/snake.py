from collections import deque

from direction import Direction


class Snake:
    def __init__(self, board_size: int) -> None:
        self.__direction = Direction.UP
        board_center = board_size // 2
        self.__positions = deque()
        self.__positions.append((board_center, board_center))
        self.__positions.append((board_center + 1, board_center))
        self.__positions.append((board_center + 2, board_center))

    def move(self, direction: Direction) -> tuple[int, int]:
        self.__positions.appendleft(self.__get_new_head(direction))
        return self.__positions.pop()

    def eat(self, direction: Direction) -> None:
        self.__positions.append(self.move(direction))

    def can_eat(self, direction: Direction, food_position: tuple[int, int]) -> bool:
        return self.__get_new_head(direction) == food_position

    @property
    def head(self) -> tuple[int, int]:
        return self.__positions[0]

    @property
    def direction(self) -> Direction:
        return self.__direction

    @property
    def positions(self) -> deque:
        return self.__positions.copy()

    @property
    def length(self) -> int:
        return len(self.__positions)

    def __get_new_head(self, direction: Direction) -> tuple[int, int]:
        if self.__direction.value != tuple(-x for x in direction.value):
            self.__direction = direction

        current_head = self.head
        return tuple(map(sum, zip(current_head, self.__direction.value)))

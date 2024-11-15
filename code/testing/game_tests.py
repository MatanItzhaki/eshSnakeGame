import unittest
from collections import deque
from unittest.mock import Mock, patch, PropertyMock

from direction import Direction
from game import Game
from snake import Snake


class GameTests(unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.__board_size = 5
        self.__num_moves = 2
        self.__foods = [(1, 1), (0, 2)]
        self.__snake = Mock(spec=Snake)
        type(self.__snake).positions = PropertyMock(return_value=deque([(2, 2), (3, 2), (4, 2)]))
        type(self.__snake).head = PropertyMock(return_value=(2, 2))
        with patch('builtins.input') as self.__input_supplier:
            self.__game = Game(self.__board_size, self.__num_moves, self.__foods, self.__snake, self.__input_supplier)

    def testSnakeLength_withSnakeMock_shouldReturnSnakeLength(self):
        # Arrange
        type(self.__snake).length = PropertyMock(return_value=4)

        # Act + Assert
        self.assertEqual(self.__game.snake_length, 4)

    def testRun_withInputMockAndWithoutPause_shouldCallInputAsNumMoves(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "2"]

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__input_supplier.call_count, self.__num_moves)

    def testRun_withInputMockAndWithPauseOnce_shouldCallInputAsNumMovesPlusTwo(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "5", "5", "2"]

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__input_supplier.call_count, self.__num_moves + 2)

    def testRun_withInputMockAndWithPauseTwice_shouldCallInputAsNumMovesPlusFour(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "5", "5", "5", "5", "2"]

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__input_supplier.call_count, self.__num_moves + 4)

    def testRun_withSnakeMockAndWithoutPause_shouldCallEatPlusMoveAsNumMoves(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "2"]

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__snake.eat.call_count + self.__snake.move.call_count, self.__num_moves)

    def testRun_withSnakeMockAndWithPauseOnce_shouldCallEatPlusMoveAsNumMoves(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "5", "5", "2"]

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__snake.eat.call_count + self.__snake.move.call_count, self.__num_moves)

    def testRun_withSnakeMockAndWithoutPause_shouldCallCanEatAsNumMoves(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "2"]

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__snake.can_eat.call_count, self.__num_moves)

    def testRun_withSnakeMockAndWithPauseOnce_shouldCallCanEatAsNumMoves(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "5", "5", "2"]

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__snake.can_eat.call_count, self.__num_moves)

    def testRun_withInvalidDirectionInput_shouldUseCurrentDirection(self):
        # Arrange
        self.__input_supplier.side_effect = ["right", "right"]
        type(self.__snake).direction = PropertyMock(return_value=Direction.UP)
        self.__snake.can_eat.return_value = False

        # Act
        self.__game.run()

        # Assert
        self.__snake.move.assert_called_with(Direction.UP)

    def testRun_withCanEatTrue_shouldCallOnlyEatAsNumMoves(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "2"]
        self.__snake.can_eat.return_value = True

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__snake.eat.call_count, self.__num_moves)
        self.assertEqual(self.__snake.move.call_count, 0)

    def testRun_withCanEatFalse_shouldCallOnlyMoveAsNumMoves(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "2"]
        self.__snake.can_eat.return_value = False

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__snake.eat.call_count, 0)
        self.assertEqual(self.__snake.move.call_count, self.__num_moves)

    def testRun_withOutOfBounds_shouldGameOverButKeepReadMoves(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "2"]
        type(self.__snake).head = PropertyMock(return_value=(-1, 2))

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__input_supplier.call_count, self.__num_moves)

    def testRun_withSnakeCollidesWithItself_shouldGameOverButKeepReadMoves(self):
        # Arrange
        self.__input_supplier.side_effect = ["2", "2"]
        type(self.__snake).positions = PropertyMock(return_value=deque([(1, 2), (1, 3), (2, 3), (2, 2), (1, 2)]))
        type(self.__snake).head = PropertyMock(return_value=(1, 2))

        # Act
        self.__game.run()

        # Assert
        self.assertEqual(self.__input_supplier.call_count, self.__num_moves)

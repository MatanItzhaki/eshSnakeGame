import unittest
from collections import deque

from direction import Direction
from snake import Snake


class SnakeTests(unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.__snake = Snake(5)

    def testInit_withAnyBoardSize_shouldSnakeHeadAtCenter(self):
        # Arrange
        expected_head = (2, 2)

        # Act
        snake = Snake(5)

        # Assert
        self.assertEqual(snake.head, expected_head)

    def testInit_withAnyBoardSize_shouldBeLengthOfThree(self):
        # Act
        snake = Snake(5)

        # Assert
        self.assertEqual(snake.length, 3)

    def testGetHead_withAnyCase_shouldReturnHead(self):
        # Arrange
        expected_head = (2, 2)

        # Act + Assert
        self.assertEqual(self.__snake.head, expected_head)

    def testGetDirection_withAnyCase_shouldReturnDirection(self):
        # Arrange
        expected_direction = Direction.UP

        # Act + Assert
        self.assertEqual(self.__snake.direction, expected_direction)

    def testGetLength_withAnyCase_shouldReturnLength(self):
        # Act + Assert
        self.assertEqual(self.__snake.length, 3)

    def testGetPositions_withAnyCase_shouldReturnPositions(self):
        # Arrange
        expected_positions = deque()
        expected_positions.append((2, 2))
        expected_positions.append((3, 2))
        expected_positions.append((4, 2))

        # Act + Assert
        self.assertEqual(self.__snake.positions, expected_positions)

    def testGetPositions_withChangeInOuterScope_shouldChangeCopyOnly(self):
        # Act
        positions = self.__snake.positions
        positions.pop()

        # Act + Assert
        self.assertNotEqual(self.__snake.positions, positions)

    def testCanEat_withClosedFoodAndValidDirection_shouldReturnTrue(self):
        # Arrange
        food_position = (1, 2)

        # Act + Assert
        self.assertTrue(self.__snake.can_eat(Direction.UP, food_position))

    def testCanEat_withClosedFoodAndOtherWayDirection_shouldReturnFalse(self):
        # Arrange
        food_position = (2, 3)

        # Act + Assert
        self.assertFalse(self.__snake.can_eat(Direction.UP, food_position))

    def testCanEat_withFarFoodAndValidDirection_shouldReturnFalse(self):
        # Arrange
        food_position = (0, 0)

        # Act + Assert
        self.assertFalse(self.__snake.can_eat(Direction.UP, food_position))

    def testCanEat_withClosedFoodAndInvalidDirection_shouldUseCurrentDirectionAndReturnTrue(self):
        # Arrange
        food_position = (1, 2)

        # Act + Assert
        self.assertTrue(self.__snake.can_eat(Direction.DOWN, food_position))

    def testCanEat_withFarFoodAndInvalidDirection_shouldUseCurrentDirectionAndReturnFalse(self):
        # Arrange
        food_position = (0, 0)

        # Act + Assert
        self.assertFalse(self.__snake.can_eat(Direction.DOWN, food_position))

    def testEat_withValidDirection_shouldIncreaseLength(self):
        # Act
        self.__snake.eat(Direction.UP)

        # Assert
        self.assertEqual(self.__snake.length, 4)

    def testEat_withValidDirection_shouldKeepTail(self):
        # Arrange
        tail = (4, 2)

        # Act
        self.__snake.eat(Direction.UP)

        # Assert
        self.assertEqual(self.__snake.positions[-1], tail)

    def testEat_withInvalidDirection_shouldIncreaseLength(self):
        # Act
        self.__snake.eat(Direction.DOWN)

        # Assert
        self.assertEqual(self.__snake.length, 4)

    def testEat_withInvalidDirection_shouldKeepTail(self):
        # Arrange
        tail = (4, 2)

        # Act
        self.__snake.eat(Direction.DOWN)

        # Assert
        self.assertEqual(self.__snake.positions[-1], tail)

    def testMove_withValidDirection_shouldNotIncreaseLength(self):
        # Act
        self.__snake.move(Direction.UP)

        # Assert
        self.assertEqual(self.__snake.length, 3)

    def testMove_withValidDirection_shouldRemoveTail(self):
        # Arrange
        tail = (4, 2)

        # Act
        self.__snake.move(Direction.UP)

        # Assert
        self.assertNotEqual(self.__snake.positions[-1], tail)

    def testMove_withInvalidDirection_shouldNotIncreaseLength(self):
        # Act
        self.__snake.move(Direction.DOWN)

        # Assert
        self.assertEqual(self.__snake.length, 3)

    def testMove_withInvalidDirection_shouldRemoveTail(self):
        # Arrange
        tail = (4, 2)

        # Act
        self.__snake.move(Direction.DOWN)

        # Assert
        self.assertNotEqual(self.__snake.positions[-1], tail)

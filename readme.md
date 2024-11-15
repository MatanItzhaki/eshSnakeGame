# Snake Game

## Installation
The game write on Python 3.10.7 without any outside libraries.

To run the same you should download Python 3.10.7 from Python website. And run the game using: Snake Game.exe


## Rules
There are some rules you need to meet:
* Init size of the snake is 3, start position is in the center of the board, moving upward.
* In each move the snake can move 90 degrees, or maintain his current directions (for
example if the snake direction is up, and you press 2, the snake will continue to move up).
* If you press a reverse direction, the snake will continue with is current direction.
* Pressing 5 pause the game, re-pressing 5 resume the game.
* After resuming the game the snake won’t move until the next line of input is entered.
* Keystrokes 2-up, 6-right, 8-down, 4-left (it’s an old phone).
* Each move present new direction the snake will move to.
* In any input who not in the keystrokes, the snake continue with is current direction.
* Each time the snake “eats” food, its length is increased by 1 from the head (the food becomes part of the snake).

## Game
In the start of the game, you should enter the number of game cases. 

For each case you should enter:
1. Board size (minimum of 5). If will you enter smaller size then 5 the game will create board with size of 5.
2. Number of moves will you play.
3. List of food positions. The game will ignore the positions that not match the board size.
4. Moves as the number was entered. For details of the valid moves - see above.

At end of each case the game print the length of the snake at the end after all the moves.

### End of game
There are some ways to finish the game:
* Play all the moves.
* Game over:
  * The snake falls off the board.
  * Snake can’t jump above itself - meaning if it collides with itself.

## Example

### Board Example
There is example for board with size of 5 will be like this:

|     |  0   |  1  |   2   |  3  |  4  |
|:---:|:----:|:---:|:-----:|:---:|:---:|
|  0  |      |     |       |     |     |
|  1  | food |     |       |     |     |
|  2  |      |     | snake |     |     |
|  3  |      |     | snake |     |     |
|  4  |      |     | snake |     |     |

The `snake` present the snake that moving up.
The `food` present the location of the food.

### Game Example
There is example for input and output for based on the board above:

input:
```
1
5
4
[(1, 2), (0, 0), (4, 4), (2, 3)]
4
4
2
2
```

output:
```
Case #1: 3
```

# PYTRIS™

Gym version of PYTRIS from [injekim](https://github.com/injekim/PYTRIS).


## Actions
RIGHT = 0
LEFT = 1
ROTATE_RIGHT = 2
ROTATE_LEFT = 3
TELEPORT = 4
HOLD = 5
SPEED_DOWN = 6

## Observation

0 - 200 : Matrix of the game (0 for empty, 1 for current piece, 2 for locked piece)
201 : Current level (0-255)
202 : next piece (0-6)
203 : holding piece (-1-6, -1 for no piece)

## Reward

Score is the reward

## Game

To play the game, run `python3 envs/pytris.py`
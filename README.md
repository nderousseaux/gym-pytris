# PYTRIS™

Gym version of PYTRIS from [injekim](https://github.com/injekim/PYTRIS).


## Exemple of use

```python
import matplotlib.pyplot as plt
import gym
import gym_pytris


env = gym.make("My-awesome-tetris-v0",  apply_api_compatibility=True)

for episode in range(10):
    env.reset()

    while True:
        env.render()
        
        action = env.action_space.sample()

        next_state, reward, done, truncated, info = env.step(action)
                    
        if done:
            break
```

## Actions
RIGHT = 0
LEFT = 1
ROTATE_RIGHT = 2
ROTATE_LEFT = 3
TELEPORT = 4
HOLD = 5
SPEED_DOWN = 6

## Observation

0 - 210 : Matrix of the game (0 for empty, 1 for current piece, 2 for locked piece)
211 : Current level (0-255)
212 : next piece (0-6)
213 : holding piece (-1-6, -1 for no piece)

## Reward

Score is the reward

## Game

To play the game, run `python3 envs/pytris.py`
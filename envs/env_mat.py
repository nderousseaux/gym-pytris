import gym
from gym import spaces
import numpy as np
from .pytris import Tetris

class EnvMat(gym.Env):
    #metadata = {'render.modes' : ['human']}
    def __init__(self):
        self.tetris = Tetris(bot=True)
        self.action_space = spaces.Discrete(7)

        

        self.observation_space = spaces.Box(
            # Array of 210 element for the matrix, 1 for the level, 1 for the next piece, 1 for the hold piece 
            np.array([0 for i in range(210)] + [0, 0, -1]),

            # Array of 210 element for the matrix, 1 for the level, 1 for the next piece, 1 for the hold piece
            np.array([2 for i in range(210)] + [255, 6, 6]),
            dtype=np.int
        )

    def reset(self):
        del self.tetris
        self.tetris = Tetris(bot=True)
        obs = self.tetris.observe()

        
        return obs

    def step(self, action):
        self.tetris.action(action) 
        obs = self.tetris.observe()
        reward = self.tetris.evaluate()
        done = self.tetris.is_done()
        return obs, reward, done, {}

    def render(self, mode="human", close=False):
        self.tetris.view()
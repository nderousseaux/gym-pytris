from gym.envs.registration import register

register(
    id='My-awesome-tetris-v0',
    entry_point='gym_mat.envs:EnvMat',
    max_episode_steps=2000,
)
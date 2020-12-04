from gym.envs.registration import register

register(
    id='atari-v0',
    entry_point='atari-breakout.envs:atariEnv',
)

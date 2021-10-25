from gym.envs.registration import register

register(
    id='Luffarschack-v0',
    entry_point='luffarschack.envs.luffarschack:LuffarschackEnv',
)

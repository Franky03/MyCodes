import gym
from time import sleep

env= gym.make('CartPole-v1', render_mode='human')

def Random_Game():
    for episode in range(10):
        env.reset()
        for t in range(500):
            action= env.action_space.sample()
            next_state, reward, done, truncated, info = env.step(action)
            env.render()
            
            print(t, next_state, reward, done, info, action)
            if(done):
                break
        


Random_Game()
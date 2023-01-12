from keras.models import Model, load_model
from keras.layers import Dense, Input
from keras.optimizers import Adam, RMSprop
import numpy as np
import gym
from collections import deque
import random

def OurModel(input_shape, action_space):
    X_input= Input(input_shape)
    # 'Dense' is the basic form of a neural network layer
    # Input Layer of state size(4) and Hidden Layer with 512 nodes
    X= Dense(512, input_shape=input_shape, activation='relu', kernel_initializer='he_uniform')(X_input)
    # Hidden layer with 256 nodes
    X= Dense(256, activation='relu', kernel_initializer='he_uniform')(X)
    # Hidden layer with 64 nodes
    X= Dense(64, activation='relu', kernel_initializer='he_uniform')(X)
    # Output Layer with # of actions: 2 nodes (left, right)
    X= Dense(action_space, activation='linear', kernel_initializer='he_uniform')(X)

    model= Model(input= X_input, outputs=X, name='CartPole DQN model')
    model.compile(loss='mse', optimizer=RMSprop(epsilon=0.01, rho=0.95, learning_rate=0.00025), metrics=["accuracy"])

    model.summary()

    return model

class DQNAgent:
    def __init__(self):
        self.env= gym.make('CartPole-v1', render_mode='human')
        self.state_size= self.env.observation_space.shape[0]
        self.action_size= self.env.action_space.n
        self.EPISODES= 1000 #número de partidas que queremos que o agente jogue
        self.memory= deque(maxlen=2000)

        self.gamma= 0.95 #taxa de decaimento ou desconto, para calcular a futura recompensa descontada
        self.epsilon= 1.0 #taxa de exploração é a taxa na qual um agente decide aleatoriamente sua ação em vez de uma previsão
        self.epsilon_min= 0.001 #queremos que o agente explore pelo menos esta quantidade
        self.epsilon_decay= 0.999 #queremos diminuir o número de explorações à medida que melhora os jogos
        self.batch_size= 64 # Determina quanta memória o DQN usará para treinar
        self.train_start= 1000 
        
        self.model= OurModel(input_shape= self.state_size, action_space=self.action_size)
    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
        if ( len(self.memory)> self.train_start ):
            if ( self.epsilon > self.epsilon_min ):
                self.epsilon *= self.epsilon_decay
    
    def replay(self):
        if ( len(self.memory) < self.train_start ):
            return
        # Randomly sample minibatch from the memory
        minibatch= random.sample(self.memory, min(len(self.memory), self.batch_size))

        state= np.zeros((self.batch_size, self.state_size))
        next_state= np.zeros((self.batch_size, self.state_size))
        action, reward, done= [], [], []

        # do this before prediction
        # for speedup, this could be done on the tensor level
        # but easier to understand using a loop

        for i in range(self.batch_size):
            state[i] = minibatch[i][0]
            action.append(minibatch[i][1])
            reward.append(minibatch[i][2])
            next_state[i] = minibatch[i][3]
            done.append(minibatch[i][4])
        
        # do batch prediction to save speed

        target= self.model.predict(state)
        target_next= self.model.predict(next_state)

        for i in range(self.batch_size):
            # correction on the Q value for the action used
            if done[i]:
                target[i][action[i]] = reward[i]
            else:
                # Standard - DQN
                # DQN chooses the max Q value among next actions
                # selection and evaluation of action is on the target Q Network
                # Q_max = max_a' Q_target(s', a')

                target[i][action[i]] = reward[i] + self.gamma * (np.max(target_next[i]))
        
        self.model.fit(state, target, batch_size= self.batch_size, verbose=0)
    
    def act(self, state):
        if np.random.random() <= self.epsilon:
            return random.randrange(self.action_size)
        else:
            return np.argmax(self.model.predict(state))
    
    def load(self, name):
        self.model = load_model(name)
    
    def save(self, name):
        self.model.save(name)
    
    def run(self):
        for e in range(self.EPISODES):
            state= self.env.reset()
            state= np.reshape(state, [1, self.state_size])
            done= False
            i=0
            while not done:
                self.env.render()
                action= self.act(state)
                next_state, reward, done, _ = self.env.step(action)
                next_state = np.reshape(next_state, [1, self.state_size])
                if not done or i== self.env._max_episode_steps-1:
                    reward = reward
                else:
                    reward = -100
                
                self.remember(state, action, reward, next_state, done)
                state = next_state
                i+=1
                
                if done:
                    print("episode: {}/{}, score: {}, e: {:.2}".format(e, self.EPISODES, i, self.epsilon))
                    if i==500:
                        print("Saving trained model as cartpole-dqn.h5")
                        self.save("cartpole-dqn.h5")
                        return
                
                self.replay()
    def test(self):
        self.load("cartpole-dqn.h5")
        for e in range(self.EPISODES):
            state= self.env.reset()
            state= np.reshape(state, [1, self.state_size])
            done= False
            i=0
            while not done:
                self.env.render()
                action= np.argmax(self.model.predict(state))
                next_state, reward, done, _ = self.env.step(action)
                next_state = np.reshape(next_state, [1, self.state_size])
                i+=1
                if done:
                    print("episode: {}/{}, score: {}".format(e, self.EPISODES, i))
                    break

if __name__ == '__main__':
    agent= DQNAgent()
    agent.run()
    #agent.test()
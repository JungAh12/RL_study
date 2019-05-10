# 파이썬과 케라스로 배우는 강화학습 #

import sys
import gym
import pylab
import random
import numpy as np
from collections import deque
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential
import keras.backend.tensorflow_backend as K

EPISODES = 300 ## 전체 에피소드 수 300

# DDQN class
class DoubleDQNAgent:
    def __init__(self, state_size, action_size):
        self.render = True                  # env.render()로 환경 visualization
        self.load_model = False             # 학습시킨 model load
        self.state_size = state_size        # state size, env.observation_space.shape[0]
        self.action_size = action_size      # action size, env.action_space.n

        # hyperparameter part
        self.discount_factor = 0.99         # gamma 값, discount factor
        self.learning_rate = 0.001          # learning rate
        self.epsilon = 1.0                  # 초기 epsilon 값 = 1
        self.epsilon_decay = 0.999          # epsilon 줄일 값
        self.epsilon_min = 0.01             # epsilon lower bound
        self.batch_size = 64                # batch size
        self.train_start = 1000             # 몇 episode 진행하고서 train 할 것인지
        self.memory = deque(maxlen=2000)    # replaymemory

        self.model = self.build_model()         # behavior network
        self.target_model = self.build_model()  # target network

        self.update_target_model()              # 초기에 target network와 behavior network의 weight가 랜덤으로 세팅되기 때문에 behavior network의 weight로 맞춰주기 위해 호출

        if self.load_model:                 # self.load_model == True, 저장해둔 모델 로드.
            self.model.load_weights("./save_model/cartpole_ddqn.h5")

    '''
    network 구성
    ---------------------

    _________________________________________________________________
    Layer (type)                 Output Shape              Param #
    =================================================================
    dense_4 (Dense)              (None, 24)                120
    _________________________________________________________________
    dense_5 (Dense)              (None, 24)                600
    _________________________________________________________________
    dense_6 (Dense)              (None, 2)                 50
    =================================================================

    <<he_uniform>>
    - Neuron의 output size를 고려하지 않는다.
    - ReLU가 0 이하의 값을 제거해버리기 때문에 분산을 2배로 줘서 분산을 유지한다는 의도.
    - [-limit, limit] 안에서의 균등분포이다.

    loss는  <<mean squar error>> 사용, optimizer는 <<Adam>> 사용

    '''

    def build_model(self):
        with K.tf.device('/gpu:0'):
            model = Sequential()
            model.add(Dense(24, input_dim=self.state_size, activation='relu',
                            kernel_initializer='he_uniform'))
            model.add(Dense(24, activation='relu',
                            kernel_initializer='he_uniform'))
            model.add(Dense(self.action_size, activation='linear',
                            kernel_initializer='he_uniform'))
            model.summary()
            model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
            return model

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights()) # copy behavior network weight -> target network weight

    def get_action(self, state):
        if np.random.rand() <= self.epsilon:                    # exploration
            return random.randrange(self.action_size)           # [0, action size] 내에서 정수 중 하나를 무작위로 리턴
        else:
            q_value = self.model.predict(state)                 # exploitation
            return np.argmax(q_value[0])                        # argmax Q(s,a)

    def append_sample(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))   # replaymemory에 tuple형식으로 저장
        if self.epsilon > self.epsilon_min:                     # e-greedy algorithm 사용
            self.epsilon *= self.epsilon_decay                  # epsilon값에 0.999 곱하면서 decaying시킴


    def train_model(self):
        if len(self.memory) < self.train_start:                 # replaymemory에 train_start(1000개)미만으로 쌓여있으면 그냥 return
            return
        batch_size = min(self.batch_size, len(self.memory))     # batch_size(64)개와 memory length 중 작은 것이 batch_size가 된다.
        mini_batch = random.sample(self.memory, batch_size)     # replaymemory에서 batch_size(64)개 만큼 sample 추출한다.

        update_input = np.zeros((batch_size, self.state_size))  # (64, 4)
        update_target = np.zeros((batch_size, self.state_size)) # (64, 4)
        action, reward, done = [], [], []

        for i in range(batch_size):                             # batch size만큼 반복
            update_input[i] = mini_batch[i][0]                  # i번째 state
            action.append(mini_batch[i][1])                     # i번째 action
            reward.append(mini_batch[i][2])                     # i번째 reward
            update_target[i] = mini_batch[i][3]                 # i번째 next_state
            done.append(mini_batch[i][4])                       # i번째 done

        target = self.model.predict(update_input)               # target = behavior network의 predict(state) 호출
        target_next = self.model.predict(update_target)         # target_next = behavior network의 predict(next_state) 호출
        target_val = self.target_model.predict(update_target)   # target_val = target network의 predict(next_state) 호출

        '''
        DDQN의 키포인트
        Y_t = R_(t+1) + gamma * Q(S_(t+1), argmax Q(S_(t+1), a; θ_t);θ'_t)

        θ_t : behavior network
        θ'_t : target network
        '''
        for i in range(self.batch_size):
            if done[i]:                                         # i번째 sample이 done == True이면
                target[i][action[i]] = reward[i]                # i번째 target[i번째 action]에 i번째 reward 값 저장, Q value 저장하는 것
            else:
                a = np.argmax(target_next[i])                   # behavior model에서 얻은 Q값 중 가장 큰 value의 index, a = argmax(Q(next_state,action))
                target[i][action[i]] = reward[i] + self.discount_factor * ( # i번째 target[i번째 action] = i번째 reward + gamma*target network의 Q(next_state,action)
                    target_val[i][a])

        # model train 시키기
        self.model.fit(update_input, target, batch_size=self.batch_size,
                       epochs=1, verbose=0)


if __name__ == "__main__":
    # 환경설정
    env = gym.make('CartPole-v1')

    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    agent = DoubleDQNAgent(state_size, action_size)

    scores, episodes = [], []

    for e in range(EPISODES):
        done = False
        score = 0
        state = env.reset()                                                 # 초기 start state 저장
        state = np.reshape(state, [1, state_size])                          # [1, state_size] shape로 변경

        while not done:
            env.render()

            action = agent.get_action(state)                                # e-greedy로 action 가져옴
            next_state, reward, done, info = env.step(action)               # 받은 action으로 step 진행
            next_state = np.reshape(next_state, [1, state_size])            # next_state도 [1, state_size] 형태로 변경
            # 에피소드가 중간에 끝나면 패널티 -100 부여
            reward = reward if not done or score == 499 else -100

            # replaymemory에 history 저장
            agent.append_sample(state, action, reward, next_state, done)
            # 매 스텝마다 train함. 대신 replaymemory에 train_start(1000개)이상 쌓여있어야 train 동작
            agent.train_model()
            score += reward
            state = next_state

            if done:        #episode 끝나면
                agent.update_target_model() # copy behavior weight -> target weight

                # 매 에피소드마다 score와 episode 저장하고 pylab.plot 그래프 그림
                score = score if score == 500 else score + 100
                scores.append(score)        # scores array에 추가
                episodes.append(e)          # episode array에 추가
                pylab.plot(episodes, scores, 'b')
                pylab.savefig("./save_graph/cartpole_ddqn.png")
                print("episode:", e, "  score:", score, "  memory length:",
                      len(agent.memory), "  epsilon:", agent.epsilon)

                # 평균 10개의 episode의 score가 490점 넘으면 실행 종료
                if np.mean(scores[-min(10, len(scores)):]) > 490:
                    sys.exit()

        # save the model
        if e % 50 == 0:
            agent.model.save_weights("./save_model/cartpole_ddqn.h5")

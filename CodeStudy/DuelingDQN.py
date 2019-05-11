import sys
import gym
import pylab
import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from collections import deque

EPISODES = 300 ## 전체 에피소드 수 300

class Model(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()

        self.fcs = nn.Sequential(
            nn.Linear(input_size, 24),
            nn.ReLU(),
        )
        self.advantage = nn.Sequential(
            nn.Linear(24, 12),
            nn.ReLU(),
            nn.Linear(12, output_size),
        )
        self.value = nn.Sequential(
            nn.Linear(24, 12),
            nn.ReLU(),
            nn.Linear(12, 1),
        )
    def forward(self, x):
        x = self.fcs(x)
        advantage = self.advantage(x)
        value     = self.value(x)
        return value + advantage  - advantage.mean()

# Dueling class
class DuelingDQNAgent():
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

        self.model = Model(state_size, action_size)         # behavior network
        self.target_model = Model(state_size, action_size)  # target network
        self.target_model.eval()

        self.optim = optim.Adam(self.model.parameters(), lr=self.learning_rate)

        self.update_target_model()          # 초기에 target network와 behavior network의 weight가 랜덤으로 세팅되기 때문에 behavior network의 weight로 맞춰주기 위해 호출

        #TODO: load and save

    def update_target_model(self):
        self.target_model.load_state_dict(self.model.state_dict())

    def get_action(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        else:
            state = torch.FloatTensor(state)
            q_value = self.model(state)
            return q_value.argmax().numpy()
    
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

        update_input = torch.FloatTensor(update_input)
        action = torch.LongTensor(np.array(action))
        reward = torch.FloatTensor(np.array(reward))
        update_target = torch.FloatTensor(update_target)
        done = torch.FloatTensor(np.array(done, dtype=np.float32))

        q = self.model(update_input)
        target_q = self.target_model(update_target)

        logits = q.gather(1, action.unsqueeze(1)).squeeze()
        target = reward + (1-done) * self.discount_factor * target_q.max(1)[0]

        loss = (logits - target).pow(2).mean()

        self.optim.zero_grad()
        loss.backward()
        self.optim.step()
        

if __name__ == "__main__":
    # 환경설정
    env = gym.make('CartPole-v1')

    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    agent = DuelingDQNAgent(state_size, action_size)

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
                pylab.pause(0.001)
                print("episode:", e, "  score:", score, "  memory length:",
                      len(agent.memory), "  epsilon:", agent.epsilon)

                # 평균 10개의 episode의 score가 490점 넘으면 실행 종료
                if np.mean(scores[-min(10, len(scores)):]) > 490:
                    env.close()
                    sys.exit()
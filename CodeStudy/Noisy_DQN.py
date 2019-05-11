import math, random

import gym
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
import torch.autograd as autograd
import torch.nn.functional as F
from torch.autograd import Variable

class NoisyLinear(nn.Module):
    def __init__(self, in_features, out_features, std_init=0.4):
        super(NoisyLinear, self).__init__()

        self.in_features  = in_features
        #input 차원
        self.out_features = out_features
        #output 차원
        self.std_init     = std_init

        #factourized gaussian noise 방법을 사용
        self.weight_mu    = nn.Parameter(torch.FloatTensor(out_features, in_features))
        self.weight_sigma = nn.Parameter(torch.FloatTensor(out_features, in_features))
        #learnable => (out*in feature 차원을 가지도록 생성)
        self.register_buffer('weight_epsilon', torch.FloatTensor(out_features, in_features))
        #epsillion은 학습에 이용 되지 않음

        self.bias_mu    = nn.Parameter(torch.FloatTensor(out_features))
        self.bias_sigma = nn.Parameter(torch.FloatTensor(out_features))
        self.register_buffer('bias_epsilon', torch.FloatTensor(out_features))
        #bias 부분

        self.reset_parameters()
        self.reset_noise()

    def forward(self, x):
        if self.training:
            weight = self.weight_mu + self.weight_sigma.mul(Variable(self.weight_epsilon))
            bias   = self.bias_mu   + self.bias_sigma.mul(Variable(self.bias_epsilon))
        else:
            weight = self.weight_mu
            bias   = self.bias_mu

        return F.linear(x, weight, bias)

    def reset_parameters(self):
        mu_range = 1 / math.sqrt(self.weight_mu.size(1))# in feature size

        self.weight_mu.data.uniform_(-mu_range, mu_range)
        #mu의 경우 independent uniform distribution에서 sampling
        self.weight_sigma.data.fill_(self.std_init / math.sqrt(self.weight_sigma.size(1)))
        #sigma를 초기화 하는 방법

        self.bias_mu.data.uniform_(-mu_range, mu_range)
        self.bias_sigma.data.fill_(self.std_init / math.sqrt(self.bias_sigma.size(0)))

        # 모델의 weight와 bias를 noise에서 sampling한 값으로 초기화

    def reset_noise(self):
        epsilon_in  = self._scale_noise(self.in_features)
        epsilon_out = self._scale_noise(self.out_features)

        self.weight_epsilon.copy_(epsilon_out.ger(epsilon_in))
        self.bias_epsilon.copy_(self._scale_noise(self.out_features))
        #noise를 reset 논문과 같음...

    def _scale_noise(self, size):
        x = torch.randn(size)
        x = x.sign().mul(x.abs().sqrt())
        #논문에서 Noise의 크기를 맞추기 위해 특정한 함수를 사용했던 부분.
        return x


class NoisyDQN(nn.Module):
    def __init__(self, num_inputs, num_actions):
        super(NoisyDQN, self).__init__()

        self.linear =  nn.Linear(env.observation_space.shape[0], 128)
        #layer로 noisyLinear 모듈을 사용
        self.noisy1 = NoisyLinear(128, 128)
        self.noisy2 = NoisyLinear(128, env.action_space.n)#output 레이어

    def forward(self, x):
        self.reset_noise()
        #매번 Noise를 만들어 주기위해 초기화 해줌. 결국 Exploration을 계속 할 수 있도록 해줌.
        x = F.relu(self.linear(x))
        x = F.relu(self.noisy1(x))
        x = self.noisy2(x)
        return x

    def act(self, state):
        state   = Variable(torch.FloatTensor(state).unsqueeze(0), volatile=True)
        q_value = self.forward(state)
        action  = q_value.max(1)[1].data[0]
        #기본 적인 Q-learning 을 따름
        return action

    def reset_noise(self):
        self.noisy1.reset_noise()
        self.noisy2.reset_noise()


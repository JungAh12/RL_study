# RL-study-2019

Value function approximation
Silver의 강의는 1~5 강과 6~10강으로 나뉜다고 생각할 수 있다.

### 1. Large-Scale Reinforcement Learning

  Reinforcement learning can be used to solve large problems, e.g.
    Backgammon  : 10^20 states
    Computer Go : 10^170 states
    Helicopter  : continous state space

#### Value Function Approximation

  So far we have represented value function by a lookup table
    Every state s has an entry V(s)
    Or overy state-action pair s,a has an engry Q(s,a)

  Problem with large MDPs:
    There are too many states and/or actions to store in memory
    It is too slow to learn the value of each state individually

  Solution for large MDPs:
    Estimate value function with function approximation
         v_hat(s,w) ~~ v_pi(s)
      or q_hat(s,a,w) ~~ q_pi(s,a)

    Generalise from seen states to unseen states
    Update parameter w using MC or TD learning

  번역
    근사 함수를 통해서, 실제 value와 실제 q를 나타내는 것
    그러기 위해서 근사 함수의 parameter인 w를 학습 시켜야하고 그때 MC or TD learning을 이용하는 것.
    이렇게 학습을 시키면, 보지 못 한 state도 본 state들로 일반화 할 수 있다.

  Which Function Approximation?
    There are many function approximations, e.g.
      Linear combinations of features
      Neural network
      Decision tree
      Nearest neighbour
      Fourier / wavelet bases
      ...

  d


















d

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

  이중에 미분을 통해 학습이 가능한, Lineaer combinations of features, Neural network 이 두가지를 보통 사용하곤 한다.

  또한, non-stationary하고 non-iid한 데이터에 적절한 training method를 사용해야 한다.

#### Incremental Methods
  Incremental (조금씩 바꿔나가는) 방법들에 대해 배울 것이다.

  Gradient descent
    Let J(w) be a differentiable function of parameter vector w
    Define the gradient of J(w) to be
      Delta_w J(w) = (w1에대한 J의 편미분, w2에 대한 J의 편미분, ...)

    To find a local minimum of J(w)
    Adjust w in direction of -ve gradient
      Delta w = -(1/2) * alpha * Delta_w J(w)
      where alpha is a step-size parameter

  Value Function Approximation By Stochastic Gradient Descent

    Goal : find parameter vector w minimising mean-squared error between approximate value function v_hat(s,w) and true value function v_pi(s)
      J(w) = E_pi[(v_pi(s) - v_hat(s,w))^2]

    Gradient descent finds a local minimum
      Delta w = -(1/2) * alpha * Delta_w J(w)
              = alpha * E_pi[(v_pi(s) - v_hat(s,w)) * Delta_w v_hat(s,w)]

    Stochastic gradient descent samples the gradient
      Delta w = alpha * (v_pi(s) - v_hat(s,w)) * Delta_w v_hat(s,w)
      기댓값을 직접 구하지 않고, Sampling을 통해 estimation 하는 것

    Expected update is equal to full gradient update

  Feature Vectors

    Represente state by a feature vector
      x(S) = (x1(S), x2(S), ... , xn(S))

    For example:
      Distance of robot from landmarks
      Trends in the stock market
      Piece and pawn configurations in chess




















d

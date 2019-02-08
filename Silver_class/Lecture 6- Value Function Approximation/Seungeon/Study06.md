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

#### Value Function Approximation By Stochastic Gradient Descent

  Goal : find parameter vector w minimising mean-squared error between approximate value function v_hat(s,w) and true value function v_pi(s)
    J(w) = E_pi[(v_pi(s) - v_hat(s,w))^2]

  Gradient descent finds a local minimum
    Delta w = -(1/2) * alpha * Delta_w J(w)
            = alpha * E_pi[(v_pi(s) - v_hat(s,w)) * Delta_w v_hat(s,w)]

  Stochastic gradient descent samples the gradient
    Delta w = alpha * (v_pi(s) - v_hat(s,w)) * Delta_w v_hat(s,w)
    기댓값을 직접 구하지 않고, Sampling을 통해 estimation 하는 것

  Expected update is equal to full gradient update

#### Feature Vectors

  Represente state by a feature vector
    x(S) = (x1(S), x2(S), ... , xn(S))

  For example:
    Distance of robot from landmarks
    Trends in the stock market
    Piece and pawn configurations in chess

  어떤 값을 나타낼 수 있는 특성이라고 생각하면 됨

#### Linear Value Function Approximation

  Represent value function by a linear combination of features
    v_hat(s,w) = x(S)^Tw = Sigma{j=1->n} xj(S)*wj

    Value라는 것이 weight들과 feature들의 내적으로 나타낼 수 있다! 라는 것이
    Linear value function approximation의 원리 그냥 Linear regression이다!!

  Objective function is quadratic in parameters w
    J(w) = E_pi[(v_pi(S) - x(S)^Tw)^2]

    목적 함수는 True value와 Estimation value 사이의 MSE!

  Stochastic gradient descent converges on global optimum
  Update rule is particularly simple
    Delta_w v_hat(S,w) = x(S)
    => 왜냐하면, 맨 처음 식에서 w에 대해 미분하면 나옴
    Delta w = alpha * (v_pi(S) - v_hat(S,w)) * x(S)
    => 왜냐하면, stochastic descent에서 이렇게 사용할 거임 x(s)가 곱해지는건

    Update = step-size * prediction error * feature value

#### Table Lookup Features

  Table lookup is a special case of linear value function approximation
  Using table lookup features
    x^table(S) = (I(S=s1), ... , I(S=sn))

  Parameter vector w gives value of each individual state
    v_hat(S,w) = (I(S=s1), ..., I(S=sn)) * (w1, ... , wn)

#### Incremental Prediction Algorithm

  Have assumed true value function v_pi(s) given by superviser
  But in RL there is no supervisor, only rewards
  In practice, we substitute a target for v_pi(s)
    For MC, the target is the return G_t
      ∆w = 𝛼 * (G_t - v_hat(St,w)) * ∇w v_hat(St,w)

    For TD(0), the target is the TD target R(t+1) + 𝛾 * v_hat(S(t+1), w)
      ∆w = 𝛼 * (R(t+1) + 𝛾 * v_hat(S(t+1), w) - v_hat(St,w)) * ∇w v_hat(St,w)

    For TD(𝜆), the garget is the 𝜆-return G^𝜆_t
      ∆w = 𝛼 * (G^𝜆_t - v_hat(St,w)) * ∇w v_hat(St,w)

  지금까지는 true value function v_pi(s)가 주어졌다고 가정했지만, RL에서는 이 true value function이 주어지지 않고, reward만이 주어진다. 그래서 실제적으로, RL에서는 v_pi(s)의 true value를 위와 같은 방법으로 가정하고 문제를 해결한다.

  MC에서는 return G_t를 사용하고, TD(0)에서는 TD error를 사용하고, TD(𝜆)에서는 𝜆-return을 사용한다고 지금까지 배웠지요?^^

#### Monte-Carlo with Value Function Approximation

  Return Gt is an unbiased, noisy sample of true value v_pi(St)
    => Return Gt는 v_pi(St)의 unbiased estimator인데 noisy하다.

  Can therefore apply supervised learning to "training data":
    <S1, G1>, <S2, G2>, ... , <ST,GT>

  For example, using linear Monte-Carlo policy evaluation
    ∆w = 𝛼 * (Gt - v_hat(St,w)) * ∇w v_hat(St,w)
       = 𝛼 * (Gt - v_hat(St,w)) * x(St)

  Monte-Carlo evaluation converges to a local optimum
  Even when using non-linear value function approximation

#### TD Learning with Value Function Approximation

  TD-target R(t+1)+ 𝛾*v_hat(S(t+1),w) is a biased sample of true value v𝜋(St)

  Can still apply supervised learning to "training data":
    <S1, R2 + 𝛾*v_hat(S2,w)>, <S2, R3 + 𝛾*v_hat(S(3),w)>, ... <S(T-1), RT>

  For example, using linear TD(0)
    ∆w = 𝛼 * (R + 𝛾*v_hat(S',w) - v_hat(St,w)) * ∇w v_hat(St,w)
       = 𝛼 * 𝛿 * x(S)

    => 영국인의 질문 R + 𝛾*v_hat(S',w)도 w로 미분이 되는데 ∆w를 저렇게 써도 되는겁니까? 안되지 않습니까?? 곱의 미분으로 해야지 않나요

  Linear TD(0) converges (close) to global optimum

#### TD(𝜆) with Value Function Approximation

  The 𝜆-return G^𝜆_t is also a biased sample of true value v_pi(s)
  Can again apply supervised learning to "training data":
    <S1, G^𝜆_1>, <S2, G^𝜆2>, ... , <S(T-1), G^𝜆(T-1)>

  Forward view linear TD(𝜆)
    ∆w = 𝛼 * (G^𝜆_t - v_hat(St,w)) * ∇w v_hat(St,w)
       = 𝛼 * (G^𝜆_t - v_hat(St,w)) * x(St)

  Backward view linear TD(𝜆)
    𝛿t = R_(t+1) + 𝛾 * v_hat(S',w) - v_hat(St,w)
    Et = 𝛾 * 𝜆 * E(t-1) + x(S_t)
    ∆w = 𝛼 * 𝛿t * Et

  Foward view and backward view linear TD(𝜆) are equivalent

#### Control with Value Function Approximation

  기존의 Dynamic programming과 다르게, 모르는 model을 풀거나 혹은 아는 model이여도 너무 클 경우에 control 문제를 Value function approximation을 통해  풀어야 하기 때문에, 다음과 같이 문제를 해결한다.

  Policy evaluation  : Approximate policy evaluation q^hat(., ., w) ≈ q_pi
  Policy improvement : e-greedy policy improvement

#### Study of lambda : Should We Bootstrap?

  Mountain Car, Random walk, Puddle world, Cart and Pole 등의 문제에서 0~1 사이 어딘가에서 가장 좋은 성능을 가지는 lambda가 존재한다. return보다, TD(0)보다 좋다는 것은 경험적으로 보여줄 수 있다.

#### Convergence of Prediction Algorithms

  On-Policy     Algorithm     Table Lookup      Linear      Non-Linear
                    MC              O             O             O
                  TD(0)             O             O             X
                TD(lambda)          O             O             X

  Off-Policy    Algorithm     Table Lookup      Linear      Non-Linear
                    MC              O             O             O
                  TD(0)             O             X             X
                TD(lambda)          O             X             X

  => On-Policy문제에서 Non-linear 문제의 경우 TD(0)와 TD(lambda) prediction에 대해 수렴이 보장 되지 않는다. (Global optimum에 가깝게 가지만 Global optimum으로 가지 못 한다.)

  => Off-Policy문제에서는 Linear와 Non-linear 문제의 경우 TD(0)와 TD(lambda) prediction에 대해 수렴이 보장되지 않는다고 한다.

#### Gradient Temporal-Difference Learning

  TD does not follow the gradient of any objective function
  This is why TD can diverge when off-policy or using non-linear function approximation
  Gradient TD follows true gradient of projected Bellman error

  => TD가 off-policy 혹은 non-linear function approximation 문제에서 발산하는 이유는 TD가 어떤 objective function의 경사를 따라가고 있지 않기 때문이다.

  => Gradient TD가 Bellman error의 true gradient를 쫓기 때문에 수렴성이 좋다고 실버 교수님이 주장중

  (Prediction)

  On-Policy     Algorithm     Table Lookup      Linear      Non-Linear
                    MC              O             O             O
                  TD(0)             O             O             X
                Gradient TD         O             O             O

  Off-Policy    Algorithm     Table Lookup      Linear      Non-Linear
                    MC              O             O             O
                  TD(0)             O             X             X
                Gradient TD         O             O             O

  (Control)
                Algorithm         Table Lookup      Linear      Non-Linear
            Monte-Carlo Control         O            (O)            X
                  Sarsa                 O            (O)            X
                Q-learning              O             X             X
            Gradient Q-learning         O             O             X

  (O)는 near-optimal value function 근처에서 왔다리 갔다리 함을 의미
  => Gradient Q-learning이 control일 때에도 수렴성이 좋다고 함ㅎ

### Batch Methods

#### Batch Reinforcement Learning

  Gradient descent is simple and appealing
  But it is not sample efficient
  Batch methods seek to find the best fitting value function
  Given the agent's experience ("training data")

  => Sample이 한번 쓰고 버려지는 비효율적인 기존의 방법을 극복하기 위해 나온 방법

#### Least Squares Prediction

  Given value function approximation v_hat(s,w) ≈ v_pi(s)
  And experience D consisting of <state, value> pairs
    D = {<s1, v1>, <s2,v2>, ... , <sT,vT>}

  Which parameteres w give the best fitting value function v_hat(s,w)?
  Least squares algorithms find parameter vector w minimising sum-squared error between v_hat(st,w) and target values v_t,
    LS(w) = Sigma {t=1->T} (v^𝜋_t - v_hat(st,w))^2
          = E_D[(v^𝜋 - v_hat(s,w))^2]

  Experience D의 v_𝜋들로 v_hat을 표현하고 싶은 것..?? 대충 D를 통해서 v_hat을 구하고 싶다 이런 느낌으로 생각해보자구~

#### Stochastic Gradient Descent with Experience Replay

  Given experience consisting of <state, value> pairs
    D = {<s1, v^𝜋1>, <s2, v^𝜋2>, ... , <ST, v^𝜋T>}

  Repeat:
    1. Sample state, value from experience
      <s,v^𝜋> ~ D

    2. Apply stochastic gradient descent update
      ∆w = alpha * (v^𝜋 - v_hat(s,w)) * Delta_w v_hat(s,w)

  Converges to least squares solution
    w^𝜋 = {w} argmin LS(w)

  => Experience replay는, Off-policy RL에서 많이 사용되고는 한다.
  => Experience replay를 사용하게 되면, LS(w)를 가장 작게만드는 w vector가 w^𝜋가 된다!

#### Experience Replay in Deep Q-Networks (DQN)

  DQN uses experience replay and fixed Q-targets
    take action a_t according to e-greedy policy
    Store transition (st, at, r(t+1), s(t+1)) in replay memory D
    Sample random mini-batch of transition (s,a,r,s') from D
    Compute Q-learning targets w.r.t. old, fixed parameteres w-
    Optimise MSE between Q-network and Q-learning targets
      Li(wi) = E_Di [(r + 𝛾 * maxQ(s',a' ; wi-) - Q(s,a ; wi))^2]

    Using variant of stochastic gradient descent

  DQN in Atari
    End-to-end learning of values Q(s,a) from pixel s
    Input state s is stack of raw pixels from last 4 frames
    Output is Q(s,a) for 18 joystick/button positions
    Reward is change in score for that step

  Network architecture and hyperparameters fixed across all games

  => RL에서의 의미 DQN이 Off-policy이고, TD이고, Neural network여서 수렴이 잘 안되는 강화학습 방법인데, Replay memory의 이용과 Fixed-Q target scheme을 이용해서, 한계를 돌파했다.

#### Linear Least Squares Prediction

  Experience replay finds least squares solution
  But it may take many iterations
  Using linear value function approximation v_hat(s,w) = x(s)^Tw
  We can solve the least squares solution directly

  At minimum of LS(w), the expected update must be zero
    E_d[Delta w] = 0
    일련의 과정을 거치면~~
    w 를 구할 수 있음. 이게 바로 Least squares method 였지?

  For N features, direct solution time is O(N^3)
  Incremental solution time is O(N^2) using Shermann - Morrison

  We do not know true values v^𝜋t
  In practice, our "training data" must use noisy or biased samples of v^𝜋t
    LSMC Least Squares Monte-Carlo uses return
      v^𝜋(t) ≈ G(t)

    LSTD Least Squares Temporal-Difference uses TD target
      v^𝜋(t) ≈ R(t+1) + gamma * v_hat(S(t+1), w)

    LSTD(lambda) Least Squares TD(lambda) uses lambda-return
      v^𝜋(t) ≈ G^𝜆(t)

  In each case solve directly for fixed point of MC / TD / TD(𝜆)









d

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

여기부터는 그냥 강의 듣거나 글쓰기 보다는 내가 읽고 이해해보자











d

# RL-study-2019
8장 까지는 MDP를 알 때 dynamic programming을 통해 문제를 푸는 방법도 배웠고, Model - free로 문제를 푸는 방법에 대해서도 배웠었다.

그래서 Prediction문제와 Control 문제를 푸는 법에 대해서 다루어 보았다.

또한 6강에서 Function approximation을 통해 문제를 scale-up하기도 해봤다ㅎㅎ

8장은 모델을 만들고, 모델을 기반으로 강화학습을 하는 문제! model을 알 때 푸는 것은 planning이고 model을 모를 때 푸는 것은 learning이라는 것을 기억하시고~~

이번 장에서는 planning과 learning을 섞는 법에 대해서도 조금 다룰 것입니다.

### Integrating Learning and Planning
바로 지난 강의에서는 경험으로부터 policy를 직접 학습했다.
그 이전의 강의에서는 value function을 경험으로 부터 직접 학습 했다.
이! 번! 엔! 경험들로 부터 model을 직접적으로 학습하는 것에 대해서 다룬다.

그 후에 모델을 통해서 value function과 policy를 constructing한다.
또한, learning과 planning을 single architecture에 integrate하는 것을 배운다.

#### Model-Free RL and Model-Based RL
Model - Free RL
  Model이 없다! 또한 경험으로 부터 Value function을 learning한다!

Model - Based RL
  경험으로 부터 model을 배운다
  model로 부터 value function 혹은 policy function을 planning한다!

#### Model-Based RL Reinforcement Learning
1. Model - based RL이란 policy가 action을 했을 때 생기는 경험을 통해서
2. model을 학습하고
3. Planning을 통해서 value와 policy를(MDP를) learn하고 solve 하는 것이다.

Advantages:
  Can efficiently learn model by supervised learning methods
  Can reason about model uncertainty
  1. spuervised learning을 통해서 model을 효율적으로 미리 학습 시킬 수 있다.
  2. 모델의 불확실성을 다룰 수 있다.

Disadvantages:
  First learn a model, then construct a value function
    => two suorces of approximation eror
    => 틀릴 수 있는 곳이 두 군데나 생긴다. 모델을 잘 못 학습하던가 value를 잘못 학습하던가 그럴 수 있다.

What is model?
  A model M is a representation of an MDP <S, A, P, R>, parameterized by n
  We will assume state space S and action space A are known
  So a model M = <Pn, Rn> represents state transitions Pn ≈ P and rewards Rn ≈ R
    S_(t+1) ≈ Pn(S_(t+1) | S_t, A_t)
    R_(t+1) = Rn(R_(t+1) | S_t, A_t)

  Typically assume conditional independence between state transitions and rewards
    P[S_(t+1), R_(t+1) | S_t, A_t] = P[S_(t+1) | S_t, A_t] * P[R_(t+1) | S_t, A_t]

Model Learning
  Goal : estimate model Mn from experience {S1, A1, R2, ... , ST}
  This is a supervised learning problem
        S1, A1 => R2, S2
        S2, A2 => R3, S3
                .
                .
                .
  S_(T-1), A_(T-1) => RT, ST

  Learning s, a -> r  is a regression problem
  Learning s, a -> s' is a density estimation problem
  Pick loss function, e.g. mean-suqared error, KL divergence and so on
  Find parameters n that minimise empirical loss

Examples of Models
  Table Lookup Model
  Linear Expectation Model
  Linear Gaussian Model
  Gaussian Process Model
  Deep Belief Network Model

Table Lookup Model
  Model is an explicit MDP, P_hat, R_hat
  각 state action pair를 방문했을 때 마다 N(s,a)를 구하고
  P_hat(a,ss')과 R_hat(s,a)를 평균을 통해 정해주는 것

  Alternatively
    각 time-step t에서 experience tuple을 기록 <St, At, R_(t+1), S_(t+1)>
    model을 sample하기 위해 tuple을 random하게 선택

#### Planning with a Model
  Given a model Mn = <Pn, Rn>
  Solve the MDP <S, A, Pn, Rn>
  Using favourite planning algorithm
    Value iteration
    Policy iteration
    Tree search
    ....

  가상의 MDP를 아는 상황이므로 VI, PI를 적용 가능

Sample - Based Planning
  A simple but powerful approach to planning
  Use the model only to generate samples
  Sample experience from model
    S_(t+1) ~ Pn(S_(t+1) | S_t, A_t)
    R_(t+1) = Rn(R_(t+1) | S_t, A_t)

  Apply model-free RL to samples e.g. :
    Monte-Carlo control
    Sarsa
    Q-learning

  Sample-based planning methods are often more efficient

  => Sample들을 model을 기반으로 마구 만들어낸 다음 model-free RL 기법을 사용하는 것
  => DP는 순진하게 전부 다 back-up하는 반면, Sample based planning은 자주 일어나는
  사건에 더 집중적으로 planning을 할 수 있고, curse of dimensionality를 해결할 수 있다.

=> Model 을 알 경우, Model을 통해서 무한한 경험들을 만들어 낼 수 있다. 그를 통해
Model - free RL을 진행하면 아주 효과가 좋아 버린다.

Planning with an inaccurate model
  Given an imperfect model <Pn, Rn> ≠ <P, R>
  Performance of model-based RL is limited to optimal policy for approximate MDP <S,A,Pn,Rn>
  i.e. Model-based RL is only as good as estimated model
  When the model is inaccurate, planning process will compute a suboptimal policy
  Solution 1
    When model is wrong, use model-free RL
  Solution 2
    reason explicitly about model uncertainty

  => model이 좋은 만 큼 model-based RL의 효과가 좋을 것이다.
  => model이 틀릴 경우, model을 안쓰고 model-free RL을 쓸 수 있을거고
  => model의 uncertainty를 표현해 줌으로써 model을 사용할 수 있다.
    예를 들어 model이 30을 출력한다 라는 것을 model이 20~40사이에서 출력한다. 라는 식

***************

### Integrated Architecture

Real and Simulated Experience
  we consider two sources of experience

  Real experience - Sampled from environment (true MDP)
    S' ~ P^a_ss'
    R  = R^a_s

  Simulated experience - Sampled from model (approximate MDP)
    S' ~ Pn(S'| S,A)
    R  = Rn(R | S,A)

Integrating Learning and Planning
  Model - Free RL
    No model
    Learn value function (and/or policy) from real experience

  Model - Based RL
    Learn a model from real experience
    Plan value function (and/or policy) from simulated experience

  Dyna
    Learn a model from experience
    Learn and plan value function (and/or policy) from real and simulated experience

Dyna-Q Algorithm
  Initialize Q(s,a) and Model(s,a) for all s and a
  Do forever:
    (a) S <- current (nonterminal) state
    (b) A <- e-greedy(S,Q)
    (c) Execute action A; observe resultant reward, R, and state, S'
    (d) Q(S,A) <- Q(S,A) + 𝛼 * [R + gamma * max{Q(S',A)} - Q(S,A)]
    (e) Model(S,A) <- R, S' (assuming deterministic environment)
    (f) Repeat n times :
        S <- random previously observed state
        A <- random action previously taken in S
        R, S' <- Model(S,A)
        Q(S,A) <- Q(S,A) + 𝛼 * [R + gamma * max{Q(S',A)} - Q(S,A)]
















ㅇ

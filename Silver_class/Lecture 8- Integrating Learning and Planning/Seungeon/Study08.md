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

#### Dyna-Q Algorithm
Dyna-Q Algorithm pseudo code
  Initialize Q(s,a) and Model(s,a) for all s and a
  Do forever:
    (a) S <- current (nonterminal) state
    (b) A <- e-greedy(S,Q)
    (c) Execute action A; observe resultant reward, R, and state, S'
    (d) Q(S,A) <- Q(S,A) + 𝛼 * [R + 𝛾 * max{Q(S',A)} - Q(S,A)]
    (e) Model(S,A) <- R, S' (assuming deterministic environment)
    (f) Repeat n times :
        S <- random previously observed state
        A <- random action previously taken in S
        R, S' <- Model(S,A)
        Q(S,A) <- Q(S,A) + 𝛼 * [R + 𝛾 * max{Q(S',A)} - Q(S,A)]

    => (e)과정은 Model learning이고 (f)과정은 model을 통한 planning!

Dyna-Q on a Simple Maze example
  아주 조금의 경험을 가지고 그걸 쥐어 짜내서 data를 효율적으로 사용하는 방법이라고
  실버 교수님이 언급 했다고 함.

***************
### Simulation-Based Search
  어떻게 Planning을 효율적으로 진행 할 건지에 대한 강의

#### Forward Search
  Forward search algorithms select the best action by lookahead
  They build a search tree with the current state s_t at the root
  Using a model of the MDP to look ahead
  No need to solve whole MDP, just sub-MDP starting from now

=> 현재 상태는 particularly important하다. 지금으로 부터의 미래만 보겠다 라는 철학
지금부터 이어지는 sub-MDP만 풀어낸다는 마인드

#### Simulation-Based Search
미래의 상황들을 sample based planning을 통해서 푸는 것
  Forward search paradigm using sample-based planning
  Simulate episodes of experience from now with the model
  Apply model-free RL to simulated episodes

=> St로부터 생성되는 많은 episode들을 simulation하는 것
=> 그렇게 생성된 simulated episode들을 기반으로 model - free RL을 적용하는 것.

  Simulate episodes of experience from now with the model
    {k=1 -> K}{s^k_t, A^k_t, R^k_(t+1), ... , S^k_T} ~ Mv

  Apply model-free RL to simulated episodes
    Monte-Carlo control -> Monte-Carlo search
    Sarsa -> TD search

#### Simple Monte-Carlo Search
  Given a model Mv and a simulation policy 𝜋
  For each action a
    Simulate K episodes from current (real) state s_t
      {k=1 -> K}{s_t, a, R^k_(t+1), S^k_(t+1), S^k_(t+1), ... , S^k_T} ~ Mv,𝜋

    Evaluate actions by mearn return (Monte-Carlo evaluation)
      Q(s_t, a) = 1/K sum(G_t) -> q𝜋(st,a)

  Select current (real) action with maximum value
    at = {a} argmax Q(st,a)

#### Monte - Carlo Tree Search (Evaluation)
  Given a model Mv
  Simulate K episodes from current state s_t using current simulation policy 𝜋
    {k=1 -> K}{s_t, a, R^k_(t+1), S^k_(t+1), S^k_(t+1), ... , S^k_T} ~ Mv,𝜋

  Build a search tree containing visited states and actions
  Evaluate states Q(s,a) by mean return of episodes from s, a
    Q(s, a) = 1/N(s,a) {k=1->K} Σ {u=t->T} Σ II(Su, Au = s,a) Gu -> q𝜋(s,a)

  After search is finished, select current (real) action with maximum value in search tree
    at = {a} argmax Q(st,a)

모든 action에 대해 뭘 하는게 아니라 현재 policy에 대해서 simulation을 하는 것.

In MCTS, the simulation policy 𝜋 improves!!
=> Monte-Carlo search의 경우는 policy가 고정 되어 있었다. 근데 MCTS는 𝜋를 개선시킴

Each simulation consists of two phase (in-tree, out-of-tree)
  Tree policy (improves): pick actions to maximise Q(S,A)
  => Q를 최대로 하는 action을 선택하는 policy (in-tree 일 경우 내가 Q 값을 아니깐)
  Default policy (fixed): pick actions randomly
  => 랜덤한 action을 선택하는 policy (out-of-tree 일 경우 내가 Q 값을 모르니깐)

Repeat (each simulation)
  Evaluate states Q(S,A) by Monte-Carlo evaluation
  Improve tree policy, e.g. by e-greedy(Q)

Monte-Carlo control applied to simulated experience
Converges on the optimal search tree, Q(S,A) -> q*(S,A)

Advantages of MC Tree Search
  Highly selective best-first search
  Evaluates states dynamically (unlike e.g. DP)
    => DP와 다르게 state를 동적으로 evaluation한다. 이 이유는 모든 state를 한번에 back up 하지 않아서.

  Uses sampling to break curse of dimensionality
    => Sampling을 통해서 차원의 저주를 부순다.

  Works for "black-box" models (only requires samples)
    => model이 black-box여도 진행이 된다.

  Computationally efficient, anytime, parallelisable
    => 계산 효율적이고, 병렬적이라는 장점이 있다.

#### Temporal - Difference Search
  Simulation-based search
  Using TD instead of MC (bootstrapping)
  MC tree search applies MC control to sub-MDP from now
  TD search applies Sarsa to sub-MDP from now

MC vs TD search
  For model-free reinforcement learning, bootstrapping is helpful
    TD learning reduces variance but increases bias
    TD learning is usually more efficient than MC
    TD(𝜆) can be much more efficient than MC

  For simulation-based search, bootstrapping is also helpful
    TD search reduces variance but increases bias
    TD search is usually more eficient than MC search
    TD(𝜆) can be much more efficient than MC search

TD Search
  Simulate episodes from the current (real) state st
  Estimate action-value function Q(s,a)
  For each step of simulation, update action-values by Sarsa
    ∆Q(S, A) = 𝛼 * (R + 𝛾 * Q(S', A') - Q(S,A))

  Select actions based on action-values Q(s,a)
    e.g. e-greedy

  May also use function approximation for Q

#### Dyna-2 앞에서 했던 Dyna의 다른 버젼
In Dyna-2, the agent stores two sets of feature weights
  Long-term memory
  Short-term (working) memory
  agent가 두개의 feature를 준비해서 Long-term memory에 관한 것은 실제 경험으로 학습
  Short-term memory의 경우 simulated experience를 통해 학습

Long-term memory is updated from real experience using TD learning
  General domain knowledge that applies to any episode

Short-term memory is updated from simulated experience using TD search
  Specific local knowledge about the current situation

Over value function is sum of long and short-term memories

***

#### 정리
모델을 학습 하는방법과, 그를 이용하는 Model-Based RL을 배웠다.
그 다음 그 Model을 아니까 Dynamic programming을 하는 방법도 배워봤고

모델을 모르는 척 하고 모델에서 sample을 simulation을 통해 얻어서 model-free RL을 해보기도 했다.

또한, real experience로 direct RL을 하고 model을 만드는 과정과
model이 만든 simulated experience로 planning하는 과정이 통합된 Dyna에 대해서도 배웠다.

마지막으로 Forward search에 대해서도 배웠다. 현재 상황에 특화해서 search하는 문제였음.
그 중에서도 Simulation-based search를 배웠다. simulation으로 현재 상황에서의 experience를 막 만들어 낸 다음 search를 하는 것.

만들어낸 experience를 Monte-Carlo method로 학습해 search하는 Monte-Carlo search도했고,

주변의 노드도 다 기억하는 Monte-Carlo Tree search도 배웠었다!

마지막으로 TD Search에 대해서도 배웠음ㅎㅎ

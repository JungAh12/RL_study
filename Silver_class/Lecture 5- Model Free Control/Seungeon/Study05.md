# RL-study-2019

Model-Free Control

### 1. Model - Free Reinforcement Learning

  Last lecture
    - Model-free prediction
    - Estimate the value function of an unknown MDP

  This lecture
    - Model-free control
    - Optimise the value function of an unknown MDP

  Model - free control을 통해 문제를 해결할 수 있는 경우
    MDP 모델을 모르더라도 경험을 샘플링 할 수 있을 경우
    MDP 모델을 알더라도 샘플을 제외하고 사용하기에는 너무 큰 경우

#### On-policy vs Off-policy

  On-policy learning
    Learn about policy pi from experience sampled from pi
    일을 실제 하면서 그를 통해 배우는 느낌

  Off-policy learning
    Learn about policy pi from experience sampled from mu
    누군가의 어깨너머로 배우는 느낌

#### Greedy vs epsilon - Greedy !

  Greedy policy improvement over V(s) requires model of MDP
    pi'(s) = {A3a} argmax R^a_s + P^a_ss' V(s')

  Greedy policy improvement over Q(s,a) is model-free
    pi'(s) = {A3a} argmax Q(s,a)

  epsilon - greedy exploration
    Simplest idea for ensuring continual exploration
    All m actions are tried with non-zero probability
    with probability 1-epsilon choose the greedy action
    with probability epsilon choose an action at random

  epsilon - greedy policy improvement
    Theorem
      For any epsilon - greedy policy pi, the epsilon - greedy policy pi' with respect to q_pi is an improvement, v_pi'(s) >= v_pi(s)

#### Monte - Carlo Control

  Every episode
    Policy evaluation Monte-Carlo policy evaluation, => Q 가 q_pi에 근사하면
    Policy improvement e-greedy policy improvement   => policy improvement

#### GLIE Monte-Carlo Control

  sample kth episode using pi : {S_1, A_1, R_2, ... S_T} ~ pi
  For each state S_t and action A_t in the episode,
    N(S_t, A_t) <- N(S_t, A_t) + 1
    Q(S_t, A_t) <- Q(S_t, A_t) + 1/N(S_t, A_t) * (G_t - Q(S_t, A_t))

  Improve policy based on new action-value function
    epsilon <- 1/k
    pi <- epsion - greedy(Q)

  Theorem
    GLIE Monte-Carlo control converges to the optimal action-value function,
    Q(s,a) -> q_*(s,a)

#### MC vs TD Control

  Temporal - differnece (TD) learning has several advantages over Monte-Carlo(MC)
    Lower variance
    Online
    Incomplete sequence

  Natural idea : use TD instead of MC in our control loop
    Apply TD to Q(S,A)
    Use epsilon-greedy policy improvement
    Update every time-step

  Updating action-value functions with Sarsa
    Q(S,A) <- Q(S,A) + alpha * (R + gamma * Q(S',A') - Q(S,A))

  TD Target : R + gamma * Q(S',A')
  TD Error  : R + gamma * Q(S',A') - Q(S,A)

#### On-Policy Control with Sarsa

  Every time-step :
    Policy evaluation Sarsa, Q ~~ q_pi
    Policy improvement, epsilon-greedy policy improvement

  Theorem
    Sarsa converges to the optimal action-value function,
    Q(s,a) -> q_*(s,a), under the following conditions:
      GLIE sequence of policies pi_t(a|s)
      Robbins-Monro sequence of step-size alpha_t
        첫 번째 식 의미 : state를 끝까지 데려간다
        두 번째 식 의미 : Q값의 update가 점점 작아져서 수렴한다

#### n-Step Sarsa

  Consider the following n-step returns for n = 1, 2, 무한 :
    n = 1   (Sarsa) q_t(1) = R_(t+1) + gamma * Q(S_(t+1))
    n = 2           q_t(2) = R_(t+1) + gamma * R_(t+2) + gamma^2 * Q(S_(t+1))
      .
      .
      .
    n = 무한  (MC)  q_t(무한) = R_(t+1) + gam * R_(t+2) + ... + gam^(T-1) * R_T

  Define the n-step Q-return
    q_t(n) = R_(t+1) + ... + gamma^(n-1) * R_(t+n) + gamma^n * Q(S_(t+n))

  n-step Sarsa updates Q(s,a) towards the n-step Q-return
    Q(S_t, A_t) <- Q(S_t, A_t) + alpha * (q_t(n) - Q(S_t, A_t))

#### Off-Policy Learning

  Evaluate target policy pi(a|s) to compute v_pi(s) or q_pi(s,a)
  While following behaviour policy mu(a|s)
    {S_1, A_1, R_2, ..., S_T} ~ mu

  Why is this important
    Learn from observing humans or other agents
    Re-use experience generated from old policies pi_1, pi_2, ..., pi_(t-1)
    Learn about optimal policy while following exploratory policy
    Learn about multiple policies while following one policy

    번역
      사람이나 다른 agent의 행동에서 배울 수 있다.
      오래된 정책들을 따랐을 때의 경험을 재 사용할 수 있다.
      탐험 정책을 따라가면서 최적 정책을 배울 수 있다.
      하나의 정책을 따르면서 여러 정책들에 대해 배울 수 있다.

#### Importance sampling

  E_(X~P) [f(X)] = Sigma{ P(X) * f(X) }
                 = Sigma{ Q(X) * (P(X)/Q(X)) * f(X)}
                 = E_(X~Q) [ (P(X)/Q(X)) * f(X)]

  Importance Sampling for Off-Policy Monte-Carlo
    Use returns generated from mu to evaluate pi
    Weight return G_t according to similarity between policies
    Multiply importance sampling corrections along whole episode
      G^(pi/mu)_t = pi(A(t)|S(t)) * pi(A(t+1)|S(t)) * ... pi(A(T)|S(T))
                    ---------------------------------------------------
                    mu(A(t)|S(t)) * mu(A(t+1)|S(t)) * ... mu(A(T)|S(T))

    Update value towards corrected return
      V(S_t) <- V(S_t) + alpha * (G^(pi/mu)_t - V(S_t))

    Connot use if mu is zero when pi is non-zero
    Importance sampling can dramatically increase variance

    문제점
    mu가 0에 가까운 숫자일 경우 G가 폭발적으로 커질 수 있다.
    mu가 0이면 큰일난다.
    mu가 너무 크면 G가 0에 가깝게 수렴해 버린다. 이런식으로 variance가 너무 크다.

  Imporatnace Sampling for Off-Policy TD
    Use TD targets generated from mu to evaluate pi
    Weight TD target R + gam * V(S') by importance sampling
    Only need a single importance sampling correction
      V(S_t) <- V(S_t) + alpha * ( {pi(At|St)/mu(At|St)} * (TD target) - V(S_t) )

    Much lower variance than Monte-Carlo importance sampling
    Policies only need to be similar over a single step

#### Q - Learning

  We now consider off-policy learning of action-values Q(s,a)
  No importance sampling is required
  Next action is chosen using behaviour policy A_(t+1) ~ mu(.|S_t)
  But we condsider alternative successor action A' ~ pi(.|S_t)
  And updates Q(S_t,A_t) towards value of alternative action
    Q(S_t, A_t) <- Q(S_t, A_t) + alpha * (R_(t+1) + gam * Q(S_(t+1), A') - Q(S_t, A_t))

  번역
    행동을 정하는 policy인 mu로써 A의 행동을 취하고,
    학습을 할 때에는 pi라는 policy에서 A'을 가져오서 그걸로 학습한다.
    하지만 행동은 mu에서 나온 A'을 취한다.

  Off-Policy Control with Q-Learning
    We now allow both behaviour and target policies to improve
    The target policy pi is greedy w.r.t Q(s,a)
      pi(S_(t+1)) = argmax Q(S_(t+1),a')

    The behaviour policy mu is e.g. e-greedy w.r.t Q(s,a)
    The Q-learning target then simplifies :
        R_(t+1) + gam * Q(S_(t+1), A')
      = R_(t+1) + gam * Q(S_(t+1), argmax Q(S_(t+1), a') )
      = R_(t+1) + max gam * (Q_S(t+1), a')

  Q-Learning Control Algorithm
    Q(S,A) <- Q(S,A) + alpha (R + gam * max Q(S', a') - Q(S,A))

  Theorem
    Q-Learning control converges to the optimal action-value function,
    Q(s,a) -> q_*(s,a)

  번역 : Q-learning이란 학습은 greedy 하게 진행하고, 탐험은 e-greedy하게 진행한다.
  매우 좋지? 그러면 결국 Q-learning control을 통해 action-value function은 optimal action -value function으로 수렴한데

#### Relationship between DP and TD

  Full Backup (DP)
    Iterative Policy Evaluation     : v_pi(s)에 대한 벨만 expectation 방정식 이용
    Iterative Q - Policy Evaluation : q_pi(s,a)에 대한 벨만 expectation 방정식 이용
    Q - Value Iteration             : q_*(s,a)에 대한 벨만 optimality 방정식 이용

  Sample Backup (TD)
    TD Learning : v_pi(s)에 대한 벨만 expectation 방정식 이용
    Sarsa       : q_pi(s,a)에 대한 벨만 expectation 방정식 이용
    Q-Learning  : q_*(s,a)에 대한 벨만 optimality 방정식 이용























a

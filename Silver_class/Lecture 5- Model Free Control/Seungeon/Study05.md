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



















a

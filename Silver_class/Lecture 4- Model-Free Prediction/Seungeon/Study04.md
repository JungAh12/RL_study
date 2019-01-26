# RL-study-2019

Model-Free Prediction

### 1. Model-Free Reinforcement Learning

  Last lecture :
    - Planning by dynamic programming
    - Solve a known MDP
      => MDP를 안다는 것은 transition과 rewards를 아는 것

  This lecture :
    - Model-free prediction
    - Estimate the value function of an unknown MDP
      => MDP를 모를때 value fucntion을 학습
      => Policy에 따른 true value를 추정 하는 문제
      => Bellman expectation eq를 가지고 푸는 것

  Next lecture :
    - Model-free control
    - Optimise the value function of an unknown MDP
    => Bellman optimality eq를 가지고 푸는 것

### 2. Monte-Carlo Reinforcement Learning

  => Monte-Carlo 기법은 쉽게 말해 경험을 통해 알게 되는 방법

  - MC methods learn directly from episodes of experience
    => 경험을 통해 직접 배운다
  - MC is model-free : no knowledge of MDP transition / rewards
  - MC learns from complete episodes : no bootstrapping
    => episode가 끝나야 return이 정해지고, 각 state에서의 value를 알 수 있다.
  - MC uses the simplest possible idea : value = mean return
  - Caveat : can only apply MC to episodic MPDs
    - All episodes must terminate
      => 끝이 있는 MDP여야 한다.

#### (1) Monte-Carlo Policy Evalutaion

  Goal : learn v_𝜋 from episodes of experience under policy 𝜋
    S_1, A_1, R_2, ..., S_k ~ 𝜋

  Recall that the return is the total discounted reward:
    G_t = R_(t+1) + 𝛾 * R_(t+2) + ... + 𝛾^(T-1) * R_T

  Recall that the value function is the expected return :
    v_𝜋(s) = E_𝜋[G_t | S_t = s]

  Monte-Carlos policy evalutation uses empirical mean return instead of expected return
  => expected return 대신에 경험적인 mean을 통해 policy evaluation을 하는 것

#### (2) First-Visit Monte-Carlo Policy Evaluation

  - To evaluate state s
  - The first time-setp t that state s is visited in an episode,
  - Increment counter N(s) <- N(s) + 1
  - Incrment total return S(s) <- S(s) + G_t
  - Value is estimated by mean return V(s) = S(s)/N(s)
  - By law of large numbers, V(s) -> v_𝜋(s) as N(s) -> ∞
    => s에 가장 처음 방문했을 때 counter를 올리고 return을 더한다.
    => V(s)는 mean return인 S(s)/N(s)로 추정한다. 큰 수의 법칙에 따라 실제 값에 수렴한다.

#### (3) Every-Visit Monte-Carlo Policy Evaluation

  - To evaluate state s
  - Every time-step t that state s is visited in an episode,
  - Increment counter N(s) <- N(s) + 1
  - Increment total return S(s) <- S(s) + G_t
  - Value is estimated by mean return V(s) = S(s)/N(s)
  - Again, V(s) -> v_𝜋(s) as N(s) -> ∞
    => 모든 방문에 대하여 N(s), S(s)를 추정에 포함하는 것

#### (4) Incremental Mean

  The mean 𝜇_1, 𝜇_2, ... of a sequence x_1, x_2, ... can be computed incrementally,

    𝜇_k = (1/k) * {j=1 => k} Σ x_j
        = (1/k) * (x_k + {j=1 => k-1} Σ x_j )
        = (1/k) * (x_k + (k-1) * 𝜇_(k-1))
        = 𝜇_(k-1) + (1/k) * (x_k - 𝜇_(k-1))

#### (5) Incremental Monte-Calro Updates

  Update V(s) incrementally after episode S_1, A_1, R_2, ... , S_T
  For each state S_t with return G_t

    N(S_t) <- N(S_t) + 1
    V(S_t) <- V(S_t) + (1/N(S_t)) * (G_t - V(S_t))

  In non-stationary problems, it can be useful to track a running mean, i.e. forget old episodes.

    V(S_t) <- V(S_t) + 𝛼 * (G_t - V(S_t))

### 3. Temporal - Difference Learning

  - TD methods learn directly from episodes of experience
  - TD is model-free : no knowledge of MDP transition / rewards
  - TD learns from incomplete episodes, by bootstrapping
  - TD updates a guess towards a guess

#### (1) MC and TD

  - Goal : learn v_𝜋 online from experience under policy 𝜋
  - Incremental every-visit Monte-Carlo
    - Update value V(S_t) toward actual return G_t
      V(S_t) <- V(S_t) + 𝛼 * (G_t - V(S_t))

  - Simplest temporal-difference learning algorithm: TD(0)
    - Update value V(S_t) toward estimated return R_(t+1) + 𝛾 * V(S_(t+1))
      V(S_t) <- V(S_t) + 𝛼 * (R_(t+1) + 𝛾 * V(S_(t+1)) - V(S_t))

    - R_(t+1) + 𝛾 * V(S_(t+1)) is called the TD target
    - 𝛿_t = R_(t+1) + 𝛾 * V(S_(t+1)) - V_(S_t) is called the TD error

#### (2) Advantages and Disadvantages of MC vs TD

  - TD can learn before knowing the final outcome
    - TD can learn online after every step
    - MC must wait until end of episode before return is known

  - TD can learn without the final outcome
    - TD can learn from incomplete sequences
    - MC can only learn from complete sequences
    - TD works in continuing (non-terminating) environments
    - MC only works for episodic (terminating) environments

#### (3) Bias / Variance Trad - Off

  - Return G_t = R_(t+1) + 𝛾 * R_(t+2) + ... + 𝛾^(T-1) * R_t is unbiased estimate of v_𝜋(S_t)
  - True TD Target R_(t+1) + 𝛾 * v_𝜋(S_(t+1)) is unbiased estimate of v_𝜋(S_t)
  - TD target is much lower variance than the return :
    - Return depends on many random actions, transitions, rewards
    - TD target depends on one random action, transition, reward

#### (4) Advantages and Disadvantages of MC vs TD (2)

  - MC has high variance, zero bias
    - Good convergence properties
    - (even with function approximation)
    - Not very sensitive to initial value
    - Very simple to understand and use

  - TD has low variance, some bias
    - Usually more efficient than MC
    - TD(0) converges to v_𝜋(s)
    - (but not always with function approximation)
    - More sensitve to initial value

### 3. Batch Monte-Carlo and Temporal Difference

  - MC and TD converge : V(s) -> v_𝜋(s) as experience -> ∞
  - But what about batch solution for finite experience?
      s^1_1, a^1_1, r^1_2, ... , S^1_T1
                  ...
      s^K_1, a^K_1, r^K_2, ... , S^K_Tk

    - e.g. Repeatedly sample episode k
    - Apply MC or TD(0) to episode k

#### (1) Certainty Equivalence















  d

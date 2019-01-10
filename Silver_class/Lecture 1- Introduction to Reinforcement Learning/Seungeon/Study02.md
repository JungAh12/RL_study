# RL-study-2019

Marcov Decision Process

1. Introduction to MDPs

  - 강화학습 문제에서 환경을 formally describe한 것
  - 대부분의 강화학습 문제는 MDP로 formailise할 수 있다.
    - MDP를 통해 최적제어 문제를 다룰 수 있다.
    - Partially observable 문제 또한 MDP로 convert할 수 있다.

2. Markov State

  - State가 Markov하다는 것은, 어떤 상태가 현재 상태에만 영향을 받아 다음 상태로 간다는 것

3. State Transition Matrix

  - For a Markov state s and successor satte s', the state transition probability is defined by
      P_ss' = P [S_(t+1) = s' | S_t = s]

  - State transition matrix P defines transition probabilities from all states s to all successor states s'

4. A Markov Process
  A Markov process is a memoryless random process, i.e. a sequence of random states S1, S2, ... with the Markov property.

    > Definition
      A Markov Process (or Markov Chain) is a tuple <S, P>
      - S is a (finite) set of states
      - P is a state transition probability matrix,
        P_ss' = P[S_(t+1) = s' | S_t = s]

5. Markov Reward Process
  A Markov reward process is a Markov chain with values.

    > Definition
      A Markov Reward Process is a tuple <S, P, R, 𝛾>
      - S is a finite set of states
      - P is a state transition probability matrix,
          P_ss' = P[S_(t+1) = s' | S_t = s]
      - R is a reward function, R_s = E[R_(t+1) | S_t = s]
      - 𝛾 is a discount factor, 𝛾 ∈ [0, 1]

6. Return

    > Definition
      The return G_t is the total discounted reward from time-step t.
        G_t = R_(t+1) + 𝛾 * R_(t+2) + ... = {k = 0 to ∞} Σ 𝛾^k * R_(t+k+1)

      - The discount 𝛾 ∈ [0, 1] is present value of future rewards
      - The value of receiving reward R after k+1 time-steps is 𝛾^k * R
      - This values immediate reward above delayed reward.
          𝛾 close to 0 leads to "myopic" evaluation
          𝛾 close to 1 leads to "far-sighted" evaluation

7. Discount factor가 필요한 이유
  Most Markov reward and decision processes are discounted. Why?

  - Mathematically convenient to discount rewards
  - Avoids infinite returns in cyclic Markov processes
  - Uncertainty about the future may not be fully represented
  - If the reward is financial, immediate rewards may earn more interset than delayed rewards
  - Animal / human behaviour shows preference for immediate reward
  - It is sometimes possible to use undiscounted Markov reward processes (i.e. 𝛾 = 1), e.g. if all sequences terminate.

8. asdf
  sdf










































asdf

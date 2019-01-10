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

8. State-value function
  The value function v(s) gives the long-term value of state s

    > Definition
      The stete value function v(s) of an MRP is the expected return starting from state s
        v(s) = E[G_t | S_t = s]

9. Bellman Equation for MRPs
  The value function can be decomposed into two parts :
    immediate reward R_(t+1)
    discounted value of successor state 𝛾 * v(S_(t+1))
      v(s) = E[G_t | S_t = s]
           = E[R_(t+1) + 𝛾 * R_(t+2) + 𝛾^2 * R_(t+2) + ... | S_t = s]
           ...
           = E[R_(t+1) + 𝛾 * G_(t+1) | S_t = s]
           = E[R_(t+1) + 𝛾 * v(S_(t+1)) | S_t = s]

      v(s) = R_s + 𝛾 * {s' ∈ S} Σ 𝑃_𝑠𝑠′ ∗ 𝑣(𝑠′)

    Vector식으로 표현을 하게 되면
      v = R + 𝛾Pv, where v is a column vector with one entry per state
      [v(1), ... , v(n)]' = [R(1), ... , R(n)]' + 𝛾 * [P_11 ... P_1n ; P_21, ... P_2n ; ... P_nn] * [v(1), ... , v(n)]'

10. Solving the Bellman Equation

   - The bellman equation is a linear euqation
   - It can be solved directly
              v = R + 𝛾Pv
      (I - 𝛾P)v = R
              v = (I - 𝛾P)^-1 * R
   - Computational complexity is O(n^3) for n states
   - Direct solution only possible for small MPRs
   - There are many iterative methods for large MRPs, e.g.
     Dynamic programming
     Monte-Carlo evaluation
     Temporal-Difference learning

11. Markov Decision Process
  A Markov decision process (MDP) is a Markov reward process with decisions.
  It is an environment in which all states are Markov.

    > Definition
      A Markov Decision Process is a tuple <S, A, P, R, 𝛾>
      - S is a finite set of states
      - A is a finite set of actions
      - P is a state transition probability matrix,
        P^a_ss' = P[S_(t+1) = s' | S_t = s, A_t = a]
      - R is a reward function, R^a_s = E[R_(t+1) | S_t = s, A_t = a]
      - 𝛾 is a discount factor 𝛾 ∈ [0, 1].

12. Policies

    > Definition
      A policy 𝜋 is a distribution over actions given states,
        𝜋(a|s) = P[A_t = a | S_t = s]

      - A policy fully defines the behaviour of an agent
      - MDP policies depend on the current state (not the history)
      - i.e. Policies are stationary (time-independent),
        A_t ~ 𝜋(∙|S_t), ∀t > 0

  - Given an MDP M = <S, A, P, R, 𝛾> and a policy 𝜋
  - The state






















asdf

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

  - For a Markov state s and successor state s', the state transition probability is defined by
      P_ss' = P [S_(t+1) = s' | S_t = s]

  - State transition matrix P defines transition probabilities from all states s to all successor states s'

4. A Markov Process

  A Markov process is a memoryless random process, i.e. a sequence of random states S1, S2, ... with the Markov property.

    > Definition

      A Markov Process (or Markov Chain) is a tuple <S, P>
      S is a (finite) set of states
      P is a state transition probability matrix,
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

10. Solving the Bellman Equation in MRPs

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
  - The state sequence S_1, S_2, ... is a Markov process <S, P^𝜋>
  - The state and reward sequence S_1, R_2, S_2, ... is a Markov reward process <S, P^𝜋, R^𝜋, 𝛾>
  - where
    P^𝜋_ss' = {a ∈ A} 𝜋(a|s) * P^a_ss'
    R^𝜋_s   = {a ∈ A} 𝜋(a|s) * R^a_s

13. Value function

    > State-value function v(s) Definition
      The state-value function v_𝜋(s) of an MDP is the expected return starting from state s, and then following polic 𝜋
        v_𝜋(s) = E_𝜋[G_t | S_t = s]

    > Action-value function q(s,a) Definition
      The action-value function q_𝜋(s,a) is the expected return starting from state s, taking action a, and then following policy 𝜋
        q_𝜋(s,a) = E_𝜋[G_t | S_t = s, A_t = a]

14. Bellman Expectaion Equation
  The state-value function can again be decomposed into immediate reward plus discounted value of successor state,

    v_𝜋(s) = E_𝜋[R_(t+1) + 𝛾 * v_𝜋(S_(t+1)) | S_t = s]

  The action-value function can similarly be decomposed.

    q_𝜋(s,a) = E_𝜋[R_(t+1) + 𝛾 * q_𝜋(S_(t+1), A_(t+1)) | S_t = s, A_t = a]

15. Bellman Expectation Equation (Matrix Form)
  The Bellman expectation equation can be expressed concisely using the induced MRP,

            v_𝜋 = R^𝜋 + 𝛾 * P^𝜋 * v_𝜋
    with direct solution
            v_𝜋 = (I - 𝛾 * P^𝜋)^-1 * R^𝜋

16. Optimal Value function

  - The optimal value function specifies the best possible performance in the MDP
  - An MDP is "solved" when we know the optimal value function

    > Definition
      The optimal state-value function v_*(s) is the maximum value function over all policies
        v_*(s) = {𝜋} max (v_𝜋(s))

      The optimal action-value function q_*(s,a) is the maximum action-value function over all policies
        q_*(s,a) = {𝜋} max (q_𝜋(s,a))

17. Optimal policy

  Define a partial ordering over policies

    𝜋 >= 𝜋' if v_𝜋(s) >= v_𝜋'(s), ∀s

    > Theorem
      For any Markov Decision Process

      - There exists an optimal policy 𝜋_* that is better than or equal to all other policies,
        𝜋_* >= ∀𝜋

      - All optimal policies achieve the optimal value function
        v_𝜋**(s) = v_**(s)

      - All optimal policies achieve the optimal action-value function,
        q_𝜋**(s,a) = q_**(s,a)

18. Finding an Optimal Policy
  An optimal policy can be found by maximising over q_*(s,a)
  q_*를 알면, 특정 상태에서 optimal action을 아는 것이므로 optimal policy를 안다고 할 수 있다.

                1    if a = {a ∈ A} argmax (q_*(s,a))
    𝜋_*(a|s) =
                0    otherwise

  - There is always a deterministic optimal policy for any MDP
  - if we know q_*(s,a), we immediately have the optimal policy

19. Bellman Optimality Equation
  The optimal value function are recursively related by the Bellman optimality equations :
    v_**(s)   = {a} max(q_**(s,a))

    q_**(s,a) = R^a_s + 𝛾 * {s' ∈ S} Σ P^a_ss' v_**(s')

    v_**(s)   = {a} max (R^a_s) + 𝛾 * {s' ∈ S} Σ P^a_ss' v_**(s')

    q_**(s,a) = R^a_s + 𝛾 * {s' ∈ S} Σ P^a_ss' q_**(s', a')

20. Solving the Bellman Optimality Equation
  - Bellman Optimality Equation is non-linear
  - No closed form solution (in general)
  - Many iterative solution methods
    - Value iteration
    - Policy iteration
    - Q-learning
    - Sarsa

21. Extensions to MDPs
  - Infinite and continous MDPs
  - Partially observable MDPs
  - Undiscounted, average reward MDPs

22. Infinite MDPs
  The following extensions are all possible:
    - Countably infinite state and/or action spaces
      - Straightforward

    - Continuous state and/or action spaces
      - Closed form for linear quadratic model (LQR)

    - Continuous time
      - Requires partial differential equations
      - Hamilton-Jacobi-Bellman (HJB) equation
      - Limiting case of Bellman equation as time-step -> 0

23. POMDPs
  A partially Observable Markov Decision Process is an MDP with hidden states.
  It is a hidden Markov model with actions.

    > Definition
      A POMDP is a tuple <S, A, O, P, R, Z, 𝛾>
        - S is a finite set of states
        - A is a finite set of actions
        - O is a finite set of observations
        - P is a state transition probability matrix
          - P^a_(ss') = P[S_(t+1) = s' | S_t = s, A_t = a]
        - R is a reward function, R^a_s = E[R_(t+1) | S_t = s, A_t = a]
        - Z is an observation function,
          - Z^a_(s', o) = P[O_(t+1) = o | S_t = s', A_t = a]
        - 𝛾 is a discount factor 𝛾 ∈ [0, 1]

24. Belief States

    > Definition
      A history H_t is a sequence of actions, observations and rewards,
        H_t = A_0, O_1, R_1, ... , A_(t-1), O_t, R_t

    > Defienition
      A belief state b(h) is a probability distribution over states, conditioned on the history h
        b(h) = (P[S_t = s^1 | H_t = h], ..., P[S_t = s^n | H_t = h])

25. Reductions of POMDPs
  - The history H_t satisfies the Markov property
  - The belief state b(H_t) satisfies the Markov property

  - A POMDP can be reduced to an (infinite) history tree
  - A POMDP can be reduced to an (infinite) belief state tree

26. Ergodic Markov Process
  An ergodic Markov process is
  - Recurrent: each state is visited an infinite number of times
  - Aperiodic: each state is visited without any systematic period

    > Theorem
      An ergodic Markov process has a limiting stationary distribution d^𝜋(s) with the property
        d^𝜋(s) = {s' ∈ S} Σ d^𝜋(s') * P_(s's)

27. Ergodic MDP
  For any policy 𝜋, an ergodic MDP has an average reward per time-step 𝜌^𝜋 that is independent of start state
    𝜌^𝜋 = {T -> ∞} lim (1/T) * E[{t=1 to T} Σ R_t]

28. Average Reward Value function
  The value function of an undiscounted, ergodic MDP can be wxpressed in terms of average reward.
  vtild_𝜋(s) is the extra reward due to starting from state s,
    vtild_𝜋(s) = E_𝜋[ {k=1 -> ∞} Σ (R_(t+k) - 𝜌^𝜋) | S_t = s]

  There is a corresponding average reward Bellman equation,
    vtild_𝜋(s) = E_𝜋[ (R_(t+1) - 𝜌^𝜋) + {k=1 -> ∞} Σ (R_(t+k+1) - 𝜌^𝜋) | S_t = s]
               = E_𝜋[ (R_(t+1) - 𝜌^𝜋) + vtild_𝜋(S_(t+1)) | S_t = s]

















d

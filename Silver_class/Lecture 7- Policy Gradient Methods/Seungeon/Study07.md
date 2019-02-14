# RL-study-2019

Policy Gradient

### Policy- Based Reinforcement Learning

  In the last lecture we approximated the value or action-value function using parameters theta,
    V𝜃(s)   ≈ V^𝜋(s)
    Q𝜃(s,a) ≈ Q^𝜋(s,a)

  A policy was generated directly from the value function
    e.g. using e-greedy

  In this lecture we will directly parameterise the policy
    𝜋𝜃(s,a) = P[a|s,𝜃]

  We will focus again on model-free reinforcement learning

  => 저번 장에서, Function approximation을 통해 value function 혹은 action value function Q값을 근사 해 보았다.
  => 또한 policy는 value function을 통해 정해지는게 보통이었다. 하지만, 이번 장에서는 policy를 직접적으로 parameterise할 것이다. 어떻게? P[a|s,𝜃]라는 식을 통해서ㅇㅇ
  => 이 방법은 model-free reinforcement learning이다.

#### Value-Based and Policy-Based RL

  Value based RL
    Value function을 학습
    Optimal value를 알면 Optimal policy를 아는 것과 같으므로 optimal value를 구함
    implicit policy (e.g. e-greedy)

  Policy based RL
    Value function을 다루지 않음
    Policy를 직접 학습

  Actor-Critic
    Value function을 학습
    Policy 또한 학습
      Actor  : 행동하는 놈 (Policy)
      Critic : 평가하는 놈 (Value function)

#### Advantages of Policy-Based RL

  Advantages:
    - 수렴 성능이 더 좋다.
    - high-dimensional or continuous action space문제를 해결하기에 효율적이다.
    - stochastic한 policy를 학습할 수 있다.
      가위바위보 같은 경우 optimal policy가 33% 33% 33%인데 그런걸 학습 가능.

  Disadvantages:
    - 일반적으로 global optimum보다 local optimum에 수렴한다.
    - Policy의 평가는 일반적으로 비효율적이고 high varaiance이다.

  Example1 : 가위바위보
    Two-player game of 가위바위보
      - 가위 > 보
      - 바위 > 가위
      - 보 > 바위

    Consider policies for iterated 가위바위보
      - A deterministic policy is easily exploited
      - A uniform random policy is optimal

  Example2 : Aliased Gridworld
    The agent cannot differentiate the grey states
    Consider features of the following form
      𝜙(s,a) = I(wall to N, a = move E)
      Feature가 완벽하지 않아서 POMDP 문제인 것
      회색 state 2개에서 똑같은 featur를 주기 때문에, 왼쪽 회색벽에서는 오른쪽으로 가야하고 오른쪽 회색벽에서는 왼쪽에서 가야하는 문제인 것이다.

    Compare value-based RL, using an approximate value function
      Q𝜃(s,a) = f(𝜙(s,a,),𝜃)

    To policy-based RL, suing parametrised policy
      𝜋𝜃(s,a) = g(𝜙(s,a,),𝜃)

    An optimal stochastic policy will randomly move E or W in grey states
      𝜋𝜃(wall to N and S, move E) = 0.5
      𝜋𝜃(wall to N and S, move W) = 0.5

    It will reach the goal state in a few steps with high probability
    Policy-based RL can learn the optimal stochastic policy

    이러한 문제에서는 회색벽일때 반반으로 움직여주는 정책이 좋다.
    Value based RL의 경우 deterministic policy를 가지고 있기 때문에 이게 불가능

    그런데, deterministic한 policy를 왜 못 쓸까? 그 이유는 Markov property를 만족하는 fully observable MDP에서는 최적의 deterministic policy가 분명히 존재하지만, 이 문제같은 Partially observable MDP문제의 경우는 그렇지 않을 수 있다.

#### Policy Objective Functions

  Goal : given policy 𝜋𝜃(s,a) with parameters 𝜃, find best 𝜃
  But how do we measure the quality of a policy 𝜋𝜃?
  In episodic environments we can use the start value
    J1(𝜃) = V^𝜋𝜃(s1) = E_𝜋𝜃[v1]

  In continuing environments we can use the average value
    JavV(𝜃) =
















d

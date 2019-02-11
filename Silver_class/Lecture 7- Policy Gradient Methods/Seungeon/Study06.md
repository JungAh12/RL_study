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
















d

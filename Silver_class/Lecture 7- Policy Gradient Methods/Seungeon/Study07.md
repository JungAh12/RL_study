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
    (첫 번째 state에서 value function을 policy의 목적함수로 잡자!)

  In continuing environments we can use the average value
    JavV(𝜃) = Σ d^𝜋𝜃(s) * V^𝜋𝜃(s)

  Or the average reward per time-step
    JavR(𝜃) = Σ d^𝜋𝜃(s) Σ 𝜋𝜃(s,a) * R(s,a)

  d^𝜋𝜃(s)는 Markov chain 𝜋의 stationary distribution이다.
  Policy 𝜋를 따라 계속 행동하다보면은 각 상태에 머무르는 확률을 구할 수 있다.
  그것이 d^𝜋𝜃(s)이다.

#### Policy Optimisation

  Policy based reinforcement learning is an optimisation problem
  Find 𝜃 that maximises J(𝜃)
  Some approaches do not use gradient
    Hill climbing
    Simplex / amoeba / Nelder Mead
    Genetic algorithms

  Greater efficiency often possible using gradient
    Gradient descent
    Conjugate gradient
    Quasi-newton

  We focus on graidnet descent, many extensions possible
  And on methods that exploit sequential structure

#### Policy Gradient
  Let J(𝜃) be any policy objective function
  Policy gradient algorithms search for a local maximum in J(𝜃) by ascending the gradient of the policy, w.r.t. parameters 𝜃
    ∆𝜃 = 𝛼∇𝜃 J(𝜃)

  Where ∇𝜃 J(𝜃) is the policy gradient
    ∇𝜃 J(𝜃) = (𝜕J(𝜃)/𝜕𝜃1 , 𝜕J(𝜃)/𝜕𝜃2, ... , 𝜕J(𝜃)/𝜕𝜃n)'

  and 𝛼 is a step-size parameter

  J에 대한 gradient로 𝜃를 업데이트!

#### Computing gradients by finite difference

  To evaluate policy gradient of 𝜋𝜃(s,a)
  For each dimension k in [1,n]
    Estimating kth partial derivative of objective function w.r.t 𝜃
    By perturbing 𝜃 by small amount e in kth dimension
      𝜕J(𝜃) / 𝜕𝜃k ≈ {J(𝜃+euk) - J(𝜃)} / e
      where uk is unit vector with 1 in kth component, 0 elsewhere

  Uses n evaluations to compute policy gradient in n dimensions
  Simple, noisy, inefficient - but sometimes effective
  Works for arbitrary policies, even if policy is not differentiable

  𝜃1, 𝜃2, ... , 𝜃n에 대해 finite difference를 통해 J 의 gradient를 구하는 것.

  실제 사용예 : Training AIBO to walk by finite difference policy gradient

#### Score Function

  We now compute the policy gradient analytically
  Assume policy 𝜋𝜃 is differentiable whenever it is non-zero
  and we know the gradient ∇𝜃 𝜋𝜃(s,a)
  Likelihood ratios exploit the following identity
    ∇𝜃 𝜋𝜃(s,a) = 𝜋𝜃(s,a) * ∇𝜃 𝜋𝜃(s,a) / 𝜋𝜃(s,a)
               = 𝜋𝜃(s,a) * ∇𝜃 log(𝜋𝜃(s,a))

  The score function is ∇𝜃 log(𝜋𝜃(s,a))

  이런 것을 Likelihood ratio trick이라고 한다. 이걸 왜 하는지를 파악하는 것이 핵심이다.

#### Softmax Policy

  We will use a softmax policy as a running example
  Weight actions using linear combination of features 𝜙(s,a)^T𝜃
  Probability of action is proportional to exponentiated weight
    𝜋𝜃(s,a) ∝ e^𝜙(s,a)^T * 𝜃

  The score function is
    ∇𝜃 log(𝜋𝜃(s,a)) = 𝜙(s,a) - E_𝜋𝜃[𝜙(s,.)]

  계산식이 생략되었긴 하지만, softmax로 policy를 정해주면 score function을 구할 수 있다는 것

#### Gaussian Policy
  In continuous action spaces, a Gaussian policy is natural
  Mean is a linear combination of state features mu(s) = 𝜙(s,a)^T * 𝜃
  Variance may be fixed 𝜎^2, or can also parameterised
  Policy is Gaussian, a ~ N(mu(s) , 𝜎^2)

  The score function is
    ∇𝜃 log(𝜋𝜃(s,a)) = (a-mu(s)) * 𝜙(s) / 𝜎^2

  계산식이 생략되었긴 하지만, Gaussian policy를 사용하면 위와 같은 score function을 구할 수 있다는 것

#### One-Step MDP

  Consider a simple class of one-step MDPs
    Starting in states s~d(s)
    Terminating after one time-step with reward r = R(s,a)

  Use likelihood ratios to compute the policy gradient
    J(𝜃) = E_𝜋𝜃[r]
         = Σ d^𝜋𝜃(s) Σ 𝜋𝜃(s,a) * R(s,a)

    ∇𝜃 J(𝜃) = Σ d^𝜋𝜃(s) Σ 𝜋𝜃(s,a) * ∇𝜃 log(𝜋𝜃(s,a)) * R(s,a)
            E_𝜋𝜃[∇𝜃 log(𝜋𝜃(s,a)) * r]

  => 아주 중요!! J(𝜃)의 gradient를 기댓값 형태로 표현할 수 있다!
  => Sampling을 통해 해결할 수 있다는 것 (Likelihood ratio trick좋지?)

#### Policy Gradient Theorem

  The policy gradient theorem generalises the likelihood ratio appraoch to multi-step MDPs
  Replaces instantaneous reward r with long-term value Q^𝜋(s,a)
  Policy gradient theorem applies to start state objective, average reward and average value objective

  Theorem
    For any differentiable policy 𝜋𝜃(s,a), for any of the policy objective functions J=J1, J_avR, or 1/(1-𝛾)JavV, the policy gradient is
      ∇𝜃 J(𝜃) = E_𝜋𝜃[∇𝜃 log(𝜋𝜃(s,a)) * Q^𝜋𝜃(s,a)]

#### Monte-Carlo Policy Gradient (REINFORCE)
  Update parameters by stochastic gradient ascent
  Using policy gradient theorem
  Using return vt as an unbiased sample of Q^𝜋𝜃(st,at)
    ∆𝜃t = 𝛼 * ∇𝜃 log(𝜋𝜃(s,a)) * vt

  Pseudo code

  function REINFORCE
    Initialise 𝜃 arbitrarily
    for each episode {s1, a1, r2, ... , s(T-1), a(T-1), rT} ~ 𝜋𝜃 do
      for t = 1 to T-1 do
       𝜃 <- 𝜃 + 𝛼 * ∇𝜃 log(𝜋𝜃(s,a)) * vt
      end for
    end for
    return 𝜃
  end function

  Monte-Cralo 기법을 사용하고 있기 때문에 Q 값 대신 returen을 쓰고 있다.

  Puck World Example
    Continuous actions exert small force on puck
    Puck is rewarded for getting close to target
    Target location is reset every 30 secodnds
    Policy is trained using variant of Monte-Carlo policy gradient

  => 주의해서 봐야할 점1 : 학습 곡선이 지그재그가 아니라 매끄럽게 올라간다는 장점이 있다 즉, stable 하다.

  => 주의해서 봐야할 점2 : variance가 너무 커서, iteration이 9*10^7 정도 되야 수렴이 된다. 즉, 학습이 느리다.

### Actor - Critic Policy Gradient









d

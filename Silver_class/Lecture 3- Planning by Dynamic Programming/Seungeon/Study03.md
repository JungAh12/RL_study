# RL-study-2019

Planning by Dynamic Programming

### 1. What is Dynamic programming

  복잡한 문제를 subproblem으로 잘게 쪼개서 푸는 것

  DP로 풀 수 있는 문제들이 지닌 특성 두 가지

    Optimal substructure => 작은 문제로 나눌 수 있어야 한다.

      - Principle of optimality applies
      - Optimal solution can be decomposed into subproblmes

    Overlapping subproblems => subproblem에 대한 솔루션들을 저장해 놨다가 쓸 수 있어야한다.

      - Subproblems recur many times
      - Solutions can be cached and reused

    Markov Decision Process는 위 두가지 특성을 만족한다.

      - Bellman equation gives recursive decomposition
      - Value function stores and reuses solutions

  Dynamic programming은 MDP의 full knowledge을 알고 있어야 한다.

  DP는 planning에 쓰인다. (Model을 알 때 푸는 문제)

    For prediction : (value function을 맞추는 문제)
      Input  : MDP
         or  : MRP
      Output : value function v_𝜋

    Or for control : (optimal policy를 맞추는 문제)
      Input  : MDP
      Output : optimal value function v_*
         and : optimal policy 𝜋_*

### 2. Dynamic programming은 여러 분야에서 쓰인다고 한다.

  - String algorithms (sequence alignment)
  - Graph algorithm (shortest path algorithms)
  - Graphical models (Viterbi algorithm)
  - Bioinformatics (lattice models)

### 3. Policy Evaluation

  Problem  : policy 𝜋를 evaluation하는 것
  Solution : iterative application of Bellman expectation backup

  v_1 -> v_2 -> ... -> v_𝜋  ==> v_1으로 부터 v_𝜋를 계산해내는것

  Using synchronous backups
    - At each iteration k+1
    - For all states s
    - Update v_(k+1)(s) from v_k(s')
    - Where s' is a successor state of s

  ==> 모든 state에 대해서, value를 update 해 가는 것

  Bellman expectation equation을 통해서 evaluation해가는 과정

  v^(k+1) = R^𝜋 + 𝛾 * P^𝜋 * v^k

  이렇게 업데이트를 해주면 R은 정확하기 때문에 반복하다보면 실제값에 수렴하게된다.

  ****예시****
    Pridiction 문제인거 알 수 있겠죠? 각 state의 value를 구하는 거니까

    action이 (1/4)로 상하좌우이고 r = -1 on all transitions 한번 움직일때마다 보상이 -1

  - Undiscounted episodic MDP
  - Nonterminal states 1, ... , 14
  - One terminal state (shown twice as shaded squares)
  - Actions leading out of the grid leave state unchanged
  - Reward is -1 until the terminal state is reached
  - Agent follows uniform random policy

### 4. How to Improve a Policy

  - Given a policy 𝜋

    - Evaluate the policy 𝜋

      v_𝜋(s) = E[R_(t+1) + 𝛾 * R_(t+2) + ... | S_t = s]

    - Improve the policy by acting greedily with respect to v_𝜋

      𝜋' = greedy(v_𝜋)

  - In small gridworld improved policy was optimal, 𝜋' = 𝜋*
  - In general, need more iterations of improvement / evaluation
  - But this process of policy iteration always converges to 𝜋*

  - This improves the value from any state s over one step,

    q_𝜋(s, 𝜋'(s)) = {a} max q_𝜋(s,a) >= q_𝜋(s, 𝜋(s)) = v_𝜋(s)
    => q_𝜋(s, 𝜋'(s)) >= v_𝜋(s)

  - It therefore improves the value function, v_𝜋'(s) >= v_𝜋(s)

    q_𝜋(s, 𝜋'(s)) = E_𝜋'[R_(t+1) + 𝛾 * v_𝜋(S_(t+1)) | S_t = s]
                 <= E_𝜋'[R_(t+1) + 𝛾 * q_𝜋(S_(t+1), 𝜋'(S_(t+1)) | S_t = s]
                 <= E_𝜋'[R_(t+1) + 𝛾 * R_(t+2) + ... | S_t = s] = v_𝜋'(s)

  - If improvements stop,

    q_𝜋(s,𝜋'(s)) = {a} max q_𝜋(s,a) = q_𝜋(s, 𝜋(s)) = v_𝜋(s)

  - Then the Bellman optimality equation has been satisfied

    v_𝜋(s) = {a} max q_𝜋(s,a)

  - Therefore v_𝜋(s) = v_*(s) for all s
  - so 𝜋 is an optimal policy

### 5. Principle of Optimality

  모든 optimal policy는 두개의 component들로 나뉜다.
  - An optimal first action A*
  - Followed by an optimal policy from successor state S'

   > Teorem (Principle of Optimality)

   A policy 𝜋(a|s) achieves the optimal value from state s, v_𝜋(s) = v_*(s), if and only if

    - For any state s' reachable from s
    - 𝜋 achieves the optimal value from state s', v_𝜋(s') = v_*(s')

    만약 s로부터 도달할 수 있는 모든 s'에 대해 𝜋가 v_𝜋(s') = v_*(s')를 만족하게 된다면 policy 𝜋(a|s)는 state s에 대해 v_𝜋(s) = v_∗(s)를 이룰 수 있다.

### 6. Deterministic Value Iteration

  - 우리가 subproblem인 v*(s')을 알게 된다면

  - solution v*(s)는 다음과 one-step look ahead를 통해 알 수 있다.
    v*(s) <== {a} max R^a_s + 𝛾 * {s} Σ P^a_(ss') * v∗(s')

  - The idea of value iteration is to apply these updates iteratively
  - Intuition : start with final rewards and work backwards
  - Still works with loopy, stochastic MDPs

### 7. Value Iteration

  - Problem  : find optimal policy 𝜋
  - Solution : iterative application of Bellman optimality backup
  - v1 -> v2 -> ... -> v*
  - Using synchronous backups
      - At each iteration k+1
      - For all states s
      - Update v_(k+1)(s) from v_k(s')

  - Convergence to v_* will be proven later
  - Unlike policy iteration, there is no explicit policy
  - Intermediate value functions may not correspond to any policy










ㅇ

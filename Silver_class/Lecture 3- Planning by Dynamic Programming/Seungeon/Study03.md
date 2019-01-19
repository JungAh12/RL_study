# RL-study-2019

Planning by Dynamic Programming

1. What is Dynamic programming

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

2. Dynamic programming은 여러 분야에서 쓰인다고 한다.

  - String algorithms (sequence alignment)
  - Graph algorithm (shortest path algorithms)
  - Graphical models (Viterbi algorithm)
  - Bioinformatics (lattice models)

3. Policy Evaluation

  Problem  : policy 𝜋를 evaluation하는 것
  Solution : iterative application of Bellman expectation backup

  v_1 -> v_2 -> ... -> v_𝜋  ==> v_1으로 부터 v_𝜋를 계산해내는것

  Using synchronous backups
    - At each iteration k+1
    - For all states s
    - Update v_(k+1)(s) from v_k(s')
    - Where s' is a successor state of s

  ==> 모든 state에 대해서, value를 update 해 가는 것





















ㅇ

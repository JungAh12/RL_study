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

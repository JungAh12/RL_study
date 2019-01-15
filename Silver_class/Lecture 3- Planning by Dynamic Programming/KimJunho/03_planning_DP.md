## 03. Planning by Dynamic Programming

##### 1) What is Dynamic Programming
- Dynamic : sequential problem
- Programming : Optimizing the program
- optimization method for sequential problem
- subproblem을 풀고, 합쳐서 solution을 만든다.
- 다시말해, 작은 문제들로 전체 solution을 낸다.
- 어떻게 적용되는가?

##### 2) Dynamic Programming의 2가지 조건
- optimal substructure 
  - 전체 문제에 대한 optimal solution을 작은 문제들로 나눠야함.(?)
  - recursive한 Bellman Equation (V(s)와 V(s')의 관계식)
 
- overlapping subproblem
  - 만약 최적의 경로가 s1-s2-s3-s4 였다면,
  - s2에서의 최적경로도 알 수 있다.(solution을 저장하고 재사용)
  
  
##### 3) Prediction & Control
- Prediction : value function 구하기
- Control : Policy 찾기

### Policy Iteration (Evaluation, Improvement)

##### 4) Policy Evaluation
- 먼저, policy $\pi$ 가 주어졌을때, value function 찾기
- Bellman Expectation Backup 활용
- backup의 의미는 위에서 말한 solution 저장 및 재사용의 의미
- sychronous backup : 모든 state에 대해 backkup 실행
- 업데이트식을 보면, 처음엔 해당식의 값은 쓰레기값이지만,
- R값이 정확한 값이기 때문에, 점차 정확해져 수렴하게 된다.

##### 5) Policy Improvement
- evaluation에서 구한 V로 greedy하게 움직인다.(argmax a)
- $q_{\pi}(s,\pi (s)$ : s에서 $\pi$가 골라준 action하나를 받고 다음부터 $\pi$를 따라간다...?
- $\pi(s) = a$가 deterministic하다는거 때문에 윗내용이 이해가 안됨.
- greedy하게 움직여서 deterministic하다는 건가?

##### Q. policy evaluation에서 $\pi$가 optimal하다면, $v_{\pi}$에 수렴할때까지 value function도 계속 돌려야할까?
- 꼭 그렇지 않다.

### Value Iteration
- optimal policy $\pi$를 찾는다.(Bellman Optimality Backup활용)


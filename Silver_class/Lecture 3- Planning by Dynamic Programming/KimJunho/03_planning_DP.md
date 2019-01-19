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
  - cached and reused되는 solution은 value를 의미
  
  
##### 3) Prediction & Control
- Prediction 문제 : value function 구하기 문제
- Control 문제 : optimal policy 찾기 문제

### Policy Iteration (Evaluation, Improvement)

##### 4) Policy Evaluation
- 먼저, policy $\pi$ 가 주어졌을때, value function 찾기
- Bellman Expectation Backup 활용
- backup의 의미는 위에서 말한 solution 저장 및 재사용의 의미
- sychronous backup : 모든 state에 대해 backkup 실행(업데이트 실행)
- 업데이트식을 보면, 처음엔 해당식의 값은 쓰레기값이지만,
- R값이 정확한 값이기 때문에, 점차 정확해져 수렴하게 된다.

##### 5) Policy Improvement
- evaluation에서 구한 V로 greedy하게 움직인다.(argmax a)
- greedy하게 움직으면 optimal에 도달하는가?
- 아래내용은 증명
- $q_{\pi}(s,\pi (s))$ : state s에서 policy가 deterministic하다면, q=v
- $\pi'$가 argmax q이기 때문에 $q_{\pi}(s,\pi (s))$보다 $q_{\pi}(s,\pi' (s))$가 크거나 같을 것이다.
- 이는 $\pi$보다 $\pi'$이 더 낫다는 의미이고 결국 q가 계속 좋아져 optimal에 이르게 된다.

##### Q. policy evaluation에서 $\pi$가 optimal하다면, $v_{\pi}$에 수렴할때까지 value function도 계속 돌려야할까?
- 이전까진 1 evaluation - 1 improvement 인줄 알았으나, (이건 value iteration과 같다.)
- k번 evaluation하고 improvement해도 optimal에 도달할 수 있다. (강의중에 perfectly reasonable하다고 언급)

### Value Iteration
- principle of optimality : s에서 s'으로 이동가능하고, s'에서 value function이 optimal이라면, s에서의 value도 optimal이다. (당연한듯?!)
- optimal policy $\pi$를 찾는다.(Bellman Optimality Backup활용)
- k=1인 policy iteration과 동일하다는데, 값이 동일하다는 의미는 아닌거 같고 동작구조가 유사하다는 의미인거 같음.
- terminal state부터 서서히 value가 update된다.
- 그러면 굳이 policy가 필요할까? policy가 중요한 이유를 모르겠다....

### advanced
- asynchronous DP : 전체 state가 아닌 선택된 state에 대해서 backup되기때문에 DP의 문제점인 계산량을 감소시킬 수 있다.
  - in-place DP : v_k(s')으로 v_{k+1}(s)가 아닌 v_k(s)를 업데이트 한다...그래도 수렴은 한다니....
  - prioritizing sweeping : bellman error가 큰 state부터 선별적으로 골라 업데이트(backup)
  - real-time DP : agent가 방문한 state만 먼저 업데이트

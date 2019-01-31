## Model-Free Control

### 0. Review
- model-free? transition probability, reward function을 모른다. (model을 모른다.)
- Control problem? optimal policy를 찾는 문제

### 1. state-action value function ; Q function
- 이전 prediction에서는 value function을 업데이트하는데 V(s)를 사용.
- 하지만, prediction에서 구한 V를 토대로 optimal policy를 구하는데 transition probability가 필요.
- argmaxQ를 구하기 위해 V를 이용해 Q를 먼저 구하는데(action selection부분)
- 여기서 transition probability가 사용됨.(자세한건 강의 슬라이드 8 첫번째 식 참고)
- **그래서 V말고 Q를 사용하자!**

### 2. epsilon greedy policy
- 충분히 exploration을 하지못한 상태에서 greedy하게 움직이게 되면,
- optimal한 값에 도달하지 못할 수 있다. (충분히 exploration해서 모든 state를 충분히 돌았을 때, V_pi에 수렴한다고 했기 때문에...)
- 이걸 해결하기 위해 epsilon greedy exploration을 도입.
- epsilon만큼은 random하게 움직이고, 1-epsilon은 greedy하게 움직이게하여 exploration을 보장한다.
- epsilon greedy하게 움직이면 policy가 improve하는가? 답은 Yes!(증명은 슬라이드 12 참고)

### 3. Monte-Carlo Iteration
- evaluation에서 Q를 Q_pi에 수렴할때까지 하지않고, 한번 evaluation후 바로 improvement로 넘긴다.
- 하지만 이것이 잘 수렴하기 위해 GLIE조건을 만족해야한다.

### 4. GLIE (Greedy in the Limit with Infinite Exploration)
- 모든 (s, a) pair를 충분히 많이 exploring해야한다. (충분한 exploration필요)
- policy가 greedy policy에 수렴해야한다.
- 하지만, epsilon을 하나의 값으로 고정해놓으면 두번째 조건을 만족하지 못함.
- 이 두 조건을 만족하는 epsilon greedy를 만들기 위해선 epsilon을 time-step에 따라 감소시켜줘야함.
- 여기서 time-step이란 Q의 업데이트 횟수를 말한다.
- 다시말해, 첫번째 evaluation-improvement 보다는 두번째 evaluation-improvement의 epsilon이 더 작아져야한다는 말이다.
- 이 GLIE 조건을 만족하면 Monte-Carlo control은 수렴한다.

### 5. TD Control and SARSA
- value function이 V에서 Q로 바뀌었기 때문에, 업데이트식이 V-->Q로 바뀐다.
- 그러면서 업데이트를 위해 <S,A,R,S',A'>이 sample로 필요하게 되고, 여기서 SARSA가 시작된다.
- iteration과정은 MC와 같다. (1 evaluation - 1 improvement)
- 다만, TD control에서는 policy가 optimal에 수렴하기위한 조건이 하나 더 추가된다.
- 먼저 MC와 같이 0) GLIE조건을 만족해야하고, Robbins-Monro 조건도 만족해야한다.
- Robbins-Monro 조건? 1) Q값이 True값으로 다가갈 수 있을만큼 step size(alpha)가 충분히 커야하고,
- 2) 이 alpha가 time step에 따라 점점 작아져야한다.(Q의 수정량이 줄어드는..?)
- 여기에 앞선 강의에서 배운 n-step/TD lambda 등이 적용될 수 있다.

### 6. Off-policy Learning
- policy를 두 개로 나눈다.(behavior / target)
- target이 evaluation과 improvement에 관여하는 policy이고,
- behavior는 단순히 episode sampling에만 관여한다.(episode만 이걸로 뽑는다.)

### 7. Importance Sampling
- policy를 두개로 나눔에 따라, 이를 value 업데이트하는데 반영해줘야한다.
- target policy / behavior policy의 비율을 곱해주는데
- MC의 경우 episode의 모든 time step에 대해 이 비율을 각각 곱하고, 각각 곱해진 비율들을 return에 곱해준다.(슬라이드 33 참고)
- 이렇게 되면, 가뜩이나 높은 MC variance가 더 커진다.
- 그래서 이보다 variance가 적은 TD를 활용한다.

### 8. Q-Learning
- 여기엔 importance sampling이 필요하지 않다.(위 설명한 내용과 조금은 다른 off policy)
- 다음 상태에서 실제로 한 행동과 evaluation(prediction)에서 한 행동이 다르다.
- SARSA는 S에서 A라는 행동을 하고, S'에서 A'라는 행동을 한다음 Q(s,a)를 업데이트하였다.
- 이렇게 되면 S'에서 한 행동 A', 여기서 얻은 Q(s',a')가 Q(s,a)에 영향을 미친다.
- 다시말해, Q(s',a')가 안좋게 나오면 Q(s,a)도 안좋아진다.
- 이런식으로 진행되다보면 agent가 일정 구역에 갇히는 현상이 발생한다.
- **Q-learning은 S'에서 실제로 뭔 행동을 하던지 상관없이 Q(s,a)의 업데이트는 maxQ(s',a')로 하자는 것이다.**
- **행동은 epsilon greedy로, Q 업데이트는 bellman optimality equation으로**

### Question?!
- 왜 importance sampling은 variance를 키우는가? 어떻게 randomness를 키우게 되는가?






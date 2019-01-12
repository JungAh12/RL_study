### Lecture 2 : Markov Decision Process

##### 1. 특징
- fullly observable한 환경(Env)에서 RL을 formalize.

##### 2. Review
- Markov Property는 과거의 history는 필요없다.
- 이전상태의 정보만 있으면 충분하다.(독립)
- State Transition Prob은 Matrix형태로 나타낼 수 있는데,
- State의 수가 N개라면, N x N Matrix형태가 된다.

##### 3. Markov Process
- Memoryless random process.
- 즉, 이전에 어떠한 과정을 거쳐서 지금 state에 도달했는지 상관없이 미래가 정의된다.
- 이는 앞서 말한 markov property(markov state)와 관련이 있다.
- 참고로 random process의 의미는 같은 state라도 가는 경로가 다름을 의미한다.(episode sampling)

##### 4. Markov Reward Process
- 주목할점은 해당 state마다 reward가 정해져있다.
- 위에서 말한 random process로 discounted reward sum을 하면 return이 된다.
- discount factor(gamma)는 미래의 불확실성을 가치에 반영한것이라고 보면 된다.
- 간혹 gamma를 1로 놓아도 풀리는 경우도 있다.(단, sequences가 terminate된다면)

##### 5. Value Function
- V(s) : Expected return starting at state s ; s에서의 total reward의 기댓값

##### 6. Markov Decision Process
- MRP와의 차이는 수식에 action a가 붙는다는 점.
- state s에서 action a를 했을 때, 
- s'에 있을 확률 = state transition probability
- 받을 reward의 기댓값 = reward function

##### 7. Bellman Equation
- V(s)와 V(s')의 관계를 보여준다.
- 강의중 표현으로는 1-step look ahead averaging

##### 7-1. Bellman Expectation Equation
- V(s)의 관계식에 아래첨자로 policy가 붙은 형태
- s, a, s'사이에서 V(s), Q(s,a), V(s')의 관계를 보는게 이해하는데 좋았음.

##### 7-2. Bellman Optimality Equation
- 취할수 있는 action 중에서 가장 q값이 큰걸 고른다.
- Bellman Expectation Equation과 다르게 matrix 형태로 표현할 수 없다.
- 이 방정식을 통해 얻은 q로 optimal policy를 찾는데,
- 확률을 몰빵해주는 형태로 policy update가 된다.
- 여기서 알아야하는 것은 optimal이라고 해서 꼭 하나만 존재해야한다는 건 아니라는 것!!

##### Question
- transition은 policy에 독립인가? 종속인가?
- 

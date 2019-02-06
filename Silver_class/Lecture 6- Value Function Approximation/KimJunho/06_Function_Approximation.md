## Value Function Approximation
- 이 방법도 prediction과 control문제의 관점에서 진행한다.
- 경험하지 못한 state의 value를 예측해보자.

| 핵심 키워드 |
| ------------- |
| Gradient Vector |
| Feature Vector |
| Experience Replay |

### Function Approximation 필요성
- 이전까진 value function을 lookup table형태로 업데이트했다.
- 하지만, State의 크키가 커지면 이전에 배운 방법론으로 푸는데 한계가 있다.
- large scale 문제에 효율적인 방법이 필요하다.
- 보지도 경험해보지도 못한 state(unseen)를 경험한 state(seen)로 예측해보자.
- value function network를 구성하고 parameter w를 조정한다.

### Function Approximation에서의 가정
- 미분가능함수(differentiable)를 가정한다.(미분이 가능해야 parameter의 업데이트가 가능하기 때문)
- 주로 사용하는 approximator는 linear combination of features(선형)와 neural network(비선형쪽).
- value가 계속해서 바뀌고, 데이터간 상관성이 높아 이에 적합한 방법을 찾아야한다.(non-stationary, non-i.i.d)

---

### Gradient Descent
- 우리의 목적은 true value(target)와 prediction value의 차이를 최소화하는 것.(error minimize)
- TD error의 제곱 = Mean Squared Error를 loss function으로 설정.
- 이 과정에서 사용되는 개념이 gradient vector.
- slide 11에 `To find a local minimum of J(w)`의 의미는 뭘까?
- 하지만 우리는 전체 True value에 대해 업데이트하지 못하기에 sample로 나온 value를 업데이트에 이용한다.(expectation 제거)

### Feature Vector
- feature vector를 왜 쓰는가? 단, vector가 아닌 scalar로 표현하면 안되는가?
- 다루고 있는 state가 크기때문에 상세한 feature로 표현을 해줘야 학습에 용이할 것 같아 그런거 같다.
- feature는 팩맨이 터널안에 있냐, 적이 앞마당을 먹었냐, 적의 멀티는 몇개인가? 등등 feature vector형태로 나타낸다.

### Linear Value Function Approximation
- feature vector와 weight vector의 내적으로 prediction을 구성.
- 위 loss function에 대입하여 SGD를 사용하면 global optimum에 도달한다고 한다...왜?
  - linear function이라 loss의 최저점이 global한점 한군데이기 때문이다. 
- table lookup은 linear combination의 한 예시였다...(정확히 뭔말인지는 모르겠다.)

  ##### Incremental Prediction Algorithms
  - 정작 실제로 우린 true value를 모른다.
  - 이를 대체하기위해 뭘 써야할까? 이전 강의에서 배운 MC, TD 등을 사용한다.
  - 각 target값을 gradient의 true value부분에 넣어준다.

  ##### Monte-Carlo with Value Function Approximation
  - MC의 경우 return을 활용하기 때문에 unbiased했고, 따라서 수렴이 잘 되었다.
  - 하지만 여기엔 non-linear value function approximation을 사용할 때, local optimum으로 수렴한다고 함.
  - 이에 대한 팡요랩의 답변은 아래와 같다.
    ```
    많은 경우 function approximator 로  non-linear 함수를 쓸 경우의 수렴성에 대해 증명된 바가 없습니다.
    하지만 mc의 경우에는 linear 함수를 쓰면 global optimum으로 간다는 것이 증명되어 있으며,
    심지어 non-linear 함수를 써도 (global 은 아니지만)local optimum 으로 간다는 뜻이기 때문입니다.
    아무 단초도 없는 것 보다 그나마 local 로라도 간다는 것이 큰 희망이 되는 것이죠
    ```
  ##### TD learning with Value Function Approximation
  - TD learning은 biased estimation이었다.
  - linear TD(0)의 경우 global optimum에 근접한다고 한다. non-linear는? 보장 안됨.
- 그 외 방법들도 똑같이 이전 강의처럼 넣어주면된다.
- V-->Q를 넣어주고, 1 evaluation-1 improvement으로 iteration을 실시한다.

### Batch RL
- 위에서 실행한 sample들은 한번쓰고 버려진다.
- 먼저, experiences(state-value pair)를 쌓는다.(off-policy)
- 그리고 이 expeirences에서 pair를 sampling하고
- SGD로 weight를 업데이트한다. (batch learning과 똑같다.)
- 이렇게 되면, 하나의 sample이 여러번 쓰이게 된다. = experience replay (loss는 least squares)

### Deep Q-Network (DQN)
- DQN은 experience replay와 fixed Q-target이 쓰인다.
- 먼저, epsilon greedy policy를 따라 action을 취해 <s,a,r,s'> transition을 replay memory에 쌓는다.
- 그리고 random mini-batch sampling을 하여 Q-learning 식을 계산하는데
- target의 weight와 prediction의 weight를 분리한다. (Fixed Q)

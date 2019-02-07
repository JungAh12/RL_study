## Policy Gradient
- 이전 강의에서는 scaled-up 된 환경에서 Value를 학습하는 방법을 배웠다.
- 이번 강의에서는 직접 policy를 학습하는 방법을 배우도록 하자. 
- Policy를 theta(parameter)로 표현해보자.(policy network)

| 핵심 키워드 |
| :----------: |
| policy gradient |
| gradient assent |
| score function |
| likelihood ratio |
| policy gradient |

### policy를 직접 학습시키면 뭐가 좋지?
- 수렴하기에 좋은 특성을 가지고 있다.
  - value-based는 잘못하면 value가 진동하거나 발산한다.
  - 이것보다는 policy를 잘 학습하면 훨씬 stable하게 value를 학습시킬수 있다.
  - policy를 smooth하게 업데이트를 하게 되면, value가 위와 같이 진동/발산하지 않는다.
  - 그래서 policy gradient를 따르면, 최소한 local optimum은 보장되어있다.
- continuous한 action space에서 효과적이다.
  - value-based로 풀게 되면, Q(s,a)를 이를 최대화하기위한 문제를 풀어야한다.(gradient assent)
  - 이러면 gradient assent를 풀고, error를 최소화하기위한 gradient descent를 또 풀어야하는...(두번 최적화시켜야한다.)
  - action마다 최적화문제를 풀게되면 굉장히 비용이 크다. 이를 policy gradient가 해결해줄 수 있다.
- stochastic policy를 학습시킬 수 있다. (가위바위보의 경우 uniform distribution이 optimal임.)
  - value-based는 determinisitc policy를 학습했다.
  - 이러면 optimal action이 여러개인 상황에서 작동하지 못한다.
  - policy gradient는 optimal stochastic policy를 학습할수 있다.
  
### 그럼 policy를 학습시키면 장땡인가?
- **일반적으로 local optimum으로 수렴한다고 한다. ----> 왜?**
- evaluation과정에서 variance가 높고 비효율적이다.
  - 비효율적이라는 말은 value가 value-based에 비해 stable하게 업데이트되기 때문에 나온 말.
  - value-based에서는 max value에 따라 움직이면서 optimum에 다가갔다면,
  - policy-based는 policy network parameter 업데이트에 따라 조금씩/천천히 수렴한다.(inefficient)
  
### Objective Function (미분 가능을 가정)
- value-based에서는 (target value - prediction)을 줄이는데 초점이 맞춰졌지만,
- policy-based에서는 policy를 기준으로 해당 policy를 따랐을때 얻는 reward/value를 objective function으로 잡는다.
- 학습자료에 3가지 형태의 objective function이 있는데 뭘 써도 상관없다고 한다.
- 그리고 여기서 추가된 개념 stationary distribution(state의 분포)이 있다.
  - **----> 이건 갑자기 왜 생겼는가?**
- 여기선 보상을 최대로 해야하기 때문에 maximize문제가 된다.

### Policy Gradient를 계산하는 방식
  ##### finite differences
  - 한 weight를 조금 움직여서 변화하는 정도를 본다.(미분값)
  - weight가 n개 있다고 하면, 한번 policy를 업데이트하는데 n번의 계산이 필요하다.
  - policy가 미분불가능하지 않아도 되지만, 계산비용이 많이드는게 단점.
  
  ##### score function
  - policy의 gradient를 구하는데,
  - policy pi가 미분가능하고, 이것의 gradient를 안다고 가정.
  - 추후 나올 관계식에서 expectation형태로 바꾸기 위해 log의 미분을 활용하여 식을 변형.
  - 기댓값형태로 바꿔주지 않으면, 모든 a에 대한 식이어서 sampling을 기반으로한 model-free와 연관성이 떨어지고
  - 계산도 쉽지 않음.

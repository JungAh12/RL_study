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
| advantage function |

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
- One-step MDP에서 E[score function x reward]형태로 나타내고,
- 이것을 one-step이 아닌 multi-step으로 접근하여 reward ---> Q로 대체(Polict gradient theorem)
- E[score function x Q function]

### REINFORCE
- sampling으로 policy network를 업데이트하는 관점으로 보면, Q를 대체해야하는데
- REINFORCE에서는 episode=sampling으로 하여 return으로 Q를 대체한다.
- **alpha x (score function x return)** 만큼 policy의 parameter를 업데이트해준다.

### Actor-Critic Algorithm
- REINFORCE는 sampling당 return을 사용하기 때문에 variance가 높다.
- 이를 줄이기 위해, network를 두개로 나눈다.(parameter 2개) = Actor-Critic
- algorithm은 아래와 같다. (policy network : theta // value function network : w)
  - 먼저, s,theta initialize하고 policy에서 action a sampling해둔다.
  - 그리고 나서 매 step마다 다음을 실행 (for문)
  - sample (reward, next action a', next state) 뽑는다.
  - 나온 action a, a'로 TD error를 구해서 delta에 저장.
  - Q(s,a)를 가져와 policy network의 parameter theta를 업데이트한다. (gradient assent)
  - 그다음 value network의 parameter w를 업데이트한다. (gradient descent)
  - a <- a', s <- s'
  - **이는 마치 policy iteration과 유사하다.**
  
### Reducing Variance using a Baseline
- 아직 variance가 크다.
  - ---->왜?
- variance를 줄이되, 기존의 policy gradient의 expectation 결과에는 변화가 없었으면 좋겠다.
- 이를 위해서 advantage function (Q(s,a) - V(s))를 loss function의 gradient에 대입한다.
- gradient 식을 전개하면, a에 대한 sum부분에서 V(s)는 기댓값이 0이다.
- 이렇게 baseline값을 빼줘서 상대적인 크기만을 비교하여 policy의 학습을 진전시키고, variance도 낮춘다.
- state s에서 a를 했을때 얼마나 더 좋은지 안좋은지를 상대적으로 볼 수 있게 된다.
  - ---> 이건 아직도 완전히 이해가 되지 않음..
- 하지만, 이러면 policy, Q, V 각각 parameter가 생겨 총 3개의 parameter를 최적화해야한다...
  - Q대신 r+V(s')으로 대체하여(TD error), advantage를 구성한다.
  - r + V(s') - V(s)에 expectation을 취하면 결국 Advantage function이 되고,
  - 이건 다시말해, **TD error는 advantage의 sample인 셈이다.**
  - 결과적으로 gradient J(theta)의 Q대신에 TD error를 넣어주면 2개의 parameter 최적화문제로 바뀐다.(Q 학습할 필요 x)

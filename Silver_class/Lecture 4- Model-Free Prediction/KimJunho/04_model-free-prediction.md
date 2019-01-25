## 4. Model-Free Prediction

| Keyword |
| ------------- |
| model-free    |
| Monte-Carlo   |
| Temporal-Difference |
| bias-variance trade off  |
| N-step TD, TD lambda |
| Eligibility Trace |

##### a. model-free prediction?
- model을 모른다. 즉 transition probability, reward function을 모른다.
- prediction = evaluation = estimated value를 학습/찾는다. (policy 고정)

### Monte-Carlo Learning (MC)

##### b. Monte-Carlo RL
- transition probability를 모르기에, Policy를 따라서 agent를 움직여본다.(끝날때까지, terminal state까지)
- 이러면 model을 몰라도 되고, 단지 agent가 움직인 episode로 학습을 한다.
- evaluation(prediction)은 episode별 state의 return을 평균내서 구한다. (empirical mean return)

##### c. first-visit MC vs every-visit MC
- 한 episode내애서 state s에 여러번 방문할 수 있는데, 최초방문만 고려하느냐 / 모든방문을 고려하느냐의 문제
- first-visit MC는 episode당 state s의 return은 1개, every-visit은 여러개
- firs-visit은 prediction시 episode별 return 평균내면되고,
- every-visit은 episode내 & 전체 episode에 대해 평균을 내주면 된다.
- 모든 state를 충분히 방문한다면(많은 episode), 둘 다 V_pi에 수렴한다.
- 둘 중에 뭘 사용하는지는 domain by domain

##### d. incremental mean
- 이걸 왜 쓰는가?
- 이걸 쓰면 이전 return들을 일일이 기억하지 않아도 된다.
- non-stationary problem에서는 시간에 따라 값이 변하기 때문에 incremental mean으로 최근 값에 더 높은 비중을 주는 형태로 사용

### Temporal Difference Learning

##### e. temporal difference prediction (TD)
- model을 몰라도 된다는 점, episode로 학습한다는점은 MC와 동일
- but, episode가 끝나야 학습이 가능한 MC에 비해 TD는 episode가 끝나지 않아도 학습이 가능함.
- 어떻게..? bootstrapping개념이 들어감. (guess by guess)
- 1 step만 가보고 받은 Reward(R_t+1)과 거기서(S_t+1)의 value estimation으로 업데이트를 한다.
- S_t+1에서의 value도 estimation인데 이걸로 S_t에서의 value를 estimation하기 때문에 guess by guess, 즉 bootstrapping이라 함.
- 이게 가능한가...? real reward가 계속 더해지기 때문에 점점 정확해지는 느낌이다.(물이 정화되는 과정?)
- Driving home 예제는 썩 좋은 예제인지 모르겠다.

### MC vs TD 비교(3가지 관점)

##### f. episodic 관점
- MC는 final outcome을 알아야 학습이 가능한 반면,
- TD는 몰라도 학습이 가능하다. (한걸음 내딛고 학습하는...)
- episode가 언제 끝날지 모르는 상황이라면, MC쓰긴 좀 그렇...

##### g. bias & variance trade off 관점
- 먼저, 여기서의 bias와 variance는 MC와 TD에 상대적으로 적용 (낮다는 건 상대적으로 낮음을 의미한다.)
**<MC>**
- MC는 state s에 대해 episode별로 얻을 수 있는 return이 다양할 것이다.(reward의 다양한 조합이 가능하기때문에)
- 다시말해, time-step t에서 얻을 수 있는 reward가 다양하다(R_t+1자체에 randomness가 존재)
- return은 reward의 합이어서 MC는 수많은 randomness의 합으로 prediction된다. 고로 variance가 크다.
- 하지만, episode가 충분히 많이 이루어지면서 return의 기댓값(평균)은 V_pi에 다가갈 것이기 때문에 bias는 낮을 것이다.
- 펑퍼짐하게 퍼진 정규분포의 모양을 떠올려 보면 좋을 거 같다. (분산이 큰 정규분포)
- 어느 하나에 biased되어있지 않다. 다양한 return이 나올 수 있기 때문에
- 하지만 평균을 구하면 하나의 값, V_pi가 나오는 것이다.(unbiased estmate of V_pi)
**<TD>**
- 반면, TD는 MC에 비해 많은 randomness를 고려하지 않기때문에 상대적으로 variance가 낮다.
- 그러나...estimation으로 estimate하기 때문에 정확한 V_pi에 완전히 수렴하지 않게 된다.(biased estimate of V_pi)
- 그럼 정확하지 않은 값으로 estimate하는게...가능한건가? silver는 운좋게도 그렇다고 한다...증명은 따로 안함
- 관련 내용은 <Reinforcement Learning : An Introduction, sutton교수책> p101 6.2절
- policy pi를 고정했을때, TD(0)가 V_pi에 수렴한다고 한다.(step size와 관련되어있는데 자세히는..잘 모르겠다...)
- MC에 비해 효율적인 계산이 가능하지만, 초기값에 따라 좌지우지될 수 있기에 초기값을 잘 설정하는게 중요하다.

**참고**
- 위의 convergence 증명은 tabular case에 대부분 적용되고, 일부는 linear function approximation에 적용.
- 이건 향후 function approximation에서 다시 등장.


##### h. markov property 활용유무 관점 (이 부분은 확실히 와닿지는 않는다.)
- TD는 Markov property를 이용하기 때문에 markov environment에 적합.
- MC는 Markov property고 뭐고 상관없이 나온 return을 평균내는 것이기 때문에 non-markov environment에 적합.

### N-step prediction

##### i. n-step TD
- 앞서 말한 TD는 1-step으로 estimate하는 1-step TD ; TD(0) 였다.
- 하지만, step수를 늘려가면서 estimate해볼수 있다.
- step수를 늘려갈수록 점차 MC와 같아진다.
- step수가 높다고 성능이 잘나오는게 아니다.(TD(0)보다 MC가 성능이 좋은 것이 아닌것처럼)
- 2-step TD + 4-step TD를 섞어서 prediction을 할 수도 있다.

##### j. TD lambda
- 모든 step의 TD를 고려할 수 있는데, 이를 TD lambda라고 한다.
- 대신 그냥 더하여 평균내지 않고, (1-lambda)*lambda^n으로 decaying시킨다.(time step이 오래될수록 영향력 감소?)
- 즉, geometric mean을 해주는 것이다.
- 이건 forward view TD lambda이다.(모든 step을 고려해야하기때문에 결국에 episode가 끝날때까지 기다려야한다.)

##### k. Backward view TD lambda
- 모든 step을 고려하되, step을 밟아나가면서 과거에 방문한 state 정보를 고려해주는 것이다.
- 여기서 방문한 state의 정보란 ? frequency(방문 횟수), recency(방문시점이 최근이냐?)
- 이 두가지 정보를 모두 고려하는 것이 **eligibility trace**!!!!
- eligibility trace를 TD(0)(=1-step TD)의 evaluation식의 TD error부분에 곱해준다.
- 이러면 최종적으로 TD lambda와 같아진다고 한다....

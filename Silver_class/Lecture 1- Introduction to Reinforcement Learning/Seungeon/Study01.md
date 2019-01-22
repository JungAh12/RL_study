# RL-study-2019

Introduction to Reinforcement Learning

1. 강화학습이란 기계학습의 일종으로, 지도학습 / 비지도 학습과는 그 궤를 달리하는 방법론이다.

  - 강화학습에는 Labeled data등의 supervisor 없고, reward signal을 통해 학습한다.
  - 이때의 reward란, objective function으로만 결정되며, 구체적인 지침(정답)이 없다.
  - 동물, 사람이 학습하듯이 Try & error => reward 를 통해서 학습하는 것.
  - Feedback이 지연될 수 있다. 어떤 action을 했을 때, 즉각적인 반응을 얻을 수 없을 수도 있다.
  - Time really matters : action의 순서(우회전 후 좌회전 or 좌회전 후 우회전)가 엄청난 영향을 끼칠 수 있다.
  - agent에서 어떤 action을 취하게 되면, 그 이후의 state가 다 바뀐다. (강화학습의 특징)


2. Reward R_t : 보상 Scalar feedback signal
  - R_t란 step t에서 agent가 얼마나 잘 했는지를 알려주는 지표(indicator)
  - 강화학습은 cumulative reward를 maximize하는 것이 목적
  - 강화학습은 reward hypothesis를 기반으로 이뤄진다.
    > reward hypothesis는 문제에 따라 달라져야 한다. 최적화에서의 objective function
  - Sequential Decision making
    > sequential한 action을 decision 하는 방법이라고 할 수 있다.


3. Agent & Environment
  - Agent는 Controller 같은 녀석 현재 관측치 O_t와 보상 R_t를 통해 action A_t+1을 취한다.
  - Action A_t+1은 environment에 직접적인 영향을 끼치고 Agent로 O_t+1과 R_t+1을 emit한다.


4. History and State
  - H_t = O1,R1,At, ... , A_t-1,O_t,R_t
  - History란 sequential한 관측치, 행동, 보상의 기록이다.
  - agent는 history를 보고 action을 정하고, environment는 observation과 reward를 방출한다.

  - State는 다음에 어떤 일이 일어날지를 결정하는 '정보'이다!
  - 공식적으로, state is a function of the history
    > 과거의 모든 걸 볼수도 있고, 일부만 볼 수도 있는 그런 느낌인 것


5. Environment의 state
  - 환경이 observation과 reward를 계산하기 위해 쓰는 정보들이 바로 state이다.
    > 자동차로 치면, 스티어링 앵글, 엑셀 페달 포지션 등 agent가 알아봤자 쓸모 없는 것들 이지만, environment가 action을 받아서 다음 상태가 되기까지에는 꼭 필요한 정보


6. Agent의 state
  - 다음 action을 해야 할 때, 필요한 정보들
    > 자동차로 치면, 현재 기어 단 수, 현재 속도, 100m 앞의 신호등 색 등
  - 예전에 있었던 reward, observation, action등의 정보를 바로 쓸 수도 있고, 가공해서 사용할 수도 있다.


7. Markov State
  - State가 Markov하다는 것은, 어떤 상태가 현재 상태에만 영향을 받아 다음 상태로 간다는 것


8. Fully Observable Environments
  - agent directly observes environment state
    > O(t) = S(t,a)
  - 자동차로 치면, 라이다가 한 바퀴 돎에따라, partially observable하게 환경을 알 수 있다.
  - POMDP (Partially Observable MDP)
    > Complete history : S(t,a) = H(t)
    > Beliefs of environment state : S(t,a) = (P[S(t,e)=s1], ... , P[S(t,e)=sn])


9. Major Components of RL
  - Policy
    > agent의 action을 정해주는 친구, state와 action을 mapping 해준다.
    > Deterministic policy: a = 𝜋(s), Stochastic policy: 𝜋(a|s) = P[A_t = a | S_t = s]가 있다.

  - Value function
    > state, action이 얼마나 좋은지를 보여주는 함수

  - Model
    > A model predics what the environment will do next~!
    > P predicts the next state => P(ss',a) = P[S(t+1) = s' | S(t) = s, A(t) = a]
    > R predicts the next (immediate) reward => P(ss',a) = E[R(t+1) | S(t) = s, A(t) = a]
    > model의 사용 유무로 RL을 model - based RL // model - free RL 로 나눈다.


10. Categorizing RL agent (1)
  - Value based agent
    > Value function만 있어도 agent의 역할을 할 수 있음 <= ?? 말이 이상한듯

  - Policy based agent
    > Policy 만 있어도 agent의 역할을 할 수 있음 <= ?? 말이 이상한듯

  - Actor - Critic
    > Policy와 Value function을 학습하는 agent


10. Categorizing RL agent (2)
  - Model-Free
    > Environment의 model을 알지 못 하더라도, Policy와 Value만 가지고 학습을 하는 것??

  - Model-Based
    > Environment의 model을 예측하여 만들어서, 그것에 근거해서 학습을 하는 것??


11. RL로 풀 수 있는 대표적인 두 가지 문제: Learning and Planning
  - Lenarning 문제는 환경에 대해 모르지만, 환경과 상호작용 하면서 Policy를 개선해나가는 문제

  - Planning 문제는 환경의 모델을 아는 경우에(R과 P가 주어진 경우) 실제로 environment를 아니까, action을 취하지 않고도, 내부적으로 computation을 통해 모든 상황을 알 수 있다.
    > 내부적인 계산을 통해 Policy를 개선해나가는 문제
    > agent의 뇌에 perfect model이 있다고 표현했음.


12. Exploration and Exploitation
  - Reinforcement learning은 Trial and Error를 통해 학습하는 학습 방법이다.
  - Environment의 경험으로부터 좋은 Policy를 discover하는 것이 목적

  - Exploration
    > Environment를 탐험해서 정보를 모으는 과정

  - Exploitation
    > 지금까지의 정보를 가지고 최선의 선택을 내리는 과정

  - Exploration, exploitation 둘 다 중요하지만, 이 둘이 Trade - off 관계에 있다는 것을 기억해라.

13. Prediction and Control
  - Prediction : 미래를 평가하는 term
    > Given a policy
    > Value function을 학습시키는 문제

  - Control : 미래를 최적화 하는 term
    > Find the best policy

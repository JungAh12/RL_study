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

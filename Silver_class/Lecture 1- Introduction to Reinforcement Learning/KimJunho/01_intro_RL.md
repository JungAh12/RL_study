## Intro to RL

#### 1. Reinforcement-Learning의 특징
- supervisor가 없고, reward signal만 존재.
- Feedback(reward) delay가 존재 --> reward가 즉각적으로 주어지지 않는다.(t+1 time step)
- sequential data여서 시간 순서가 중요.
- agent의 action에 따라 다음 데이터가 달라짐.


#### 2. 용어
##### 1) Reward
- Scalar feedback signal --> reward의 총합을 최대로 만드는게 목적
- reward hypothesis를 잘 설정해야함
- 예를들어, '로봇이 잘 걷기위해선 서있을때 reward +1, 넘어지면 -100' 과 같이 reward hypothesis 설정이 중요

##### 2) Agent & Environment
<center><img src="/assets/RL1.PNG"></center>

- Agent가 생각하고 행동하는 주체 ; 예를들면 알고리즘
- Environment는 Agent에게 무언가를 제공해주는 곳(?)
- 서로 상호작용.

#### 3) History & State
- 위 그림의 observation, action, reward... 상호작용의 기록을 history라 함.
- state는 Agent state, Environment state가 있음.
- Markov state는 아래의 식과 같이 바로 직전의 상황만 중요한 상태를 말함.
<center><img src="/assets/markov_state.PNG"></center>


#### 4) Fully Observable Environment
- Agent가 Environment state를 볼 수 있는 경우
- 이러한 경우, Agent state = Environment(information) state
- 이를 Markov Decision Process (MDP)라 함.

#### 5) Partially Observable Environment
- 반대로 Agent state != Environment(information) state
- 간단히 말해, 상대방의 패를 볼 수 없는 포커게임이나, 배그에서 뒷치기 당하는 상황이라 할 수 있음.
- 이를 Partially Observable Markov Decision Process.
- 이때, Agent는 자신만의 state representation을 만들어야함.

### *Agent의 구성요소

#### 6) Policy($\pi$)
- Agent의 행동을 규정하는 것 ; state를 넣어주면 action을 뽑아냄.
<center><img src="/assets/policy.PNG"></center>

#### 7) Value Function
- 현재 state가 좋은지를 알려주는 지표.
- prediction of future reward
<center><img src="/assets/value_function.PNG"></center>

#### 8) Model
- Environment를 예측 ; 다음 state 예측 / reward 예측
<center><img src="/assets/model.PNG"></center>

#### 3. Agent의 종류
- Value-Based (Only Value Function)
- Policy-Based (Only Policy)
- Actor Critic (Policy + Value Function)
- Model Free (Policy/Value Function without model)
- Model Based (Policy/Value Function with model)

#### 4. Learning and Planning
- Reinforcement Learning : Environment가 어떤지 모름 ; 상호작용하면서 policy 개선
- Planning : Environment를 알고 있음. 즉, Model을 앎

#### 5. Exploration and Exploitation
- 더 많은 Environment에 대한 정보를 얻기위해 떠나는 모험 (=Exploration)
- 모은 정보 / 지금 가지고 있는 정보를 바탕으로 최선의 선택 (=Exploitation)

#### 6. prediction and Control problem
- 미래를 평가함. 즉, value function을 학습시키는 문제. (Prediction)
- 미래를 최적화시킴. 즉, 최고의 policy를 찾는 문제 (Control)

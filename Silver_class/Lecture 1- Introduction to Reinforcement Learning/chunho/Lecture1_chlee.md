# RL Course by David Silver - Lecture 1: Introduction to Reinforcement Learning


# About RL
## 강화학습과 ML의 차이점
* No supervisor, only a reward signal
* Feedback이 늦어질 수 있음 = reward
* 시간이 중요 = sequential data 순서가 중요
* Agent action이 이후에 우리가 갖게 되는 데이터에 영향을 미침 -> data fitting에 따라 달라짐

## 강화학습 용어
### Reward 
* R_t는 스칼라(숫자 하나) feedback signal
* 축척된 Reward를 최대화 하는게 Agent의 목적
* 벡터화된 데이터를 Reward를 적용하고자 한다면, 각 결과값에 임의의 가중치 같은 것들을 만들어서 계산하여 스칼라로 치환하면 적용 가능
* Reward 예시
<img src='https://www.dropbox.com/s/j8lciu46luizdav/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2014.01.34.png?raw=1'>
* Sequential Decision Making
<img src='https://www.dropbox.com/s/ygsnp7kn8dpc1ul/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2014.03.53.png?raw=1'>

### Agent, Environment
* Agent : 뇌과 같이 생각하는 머신
* Environment : Agent 밖에 있는 모든 것
<img src='https://www.dropbox.com/s/k0hobvkwx1x1q72/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2014.06.14.png?raw=1'>

### History, State
* History : `h_t`로 표현, Agent 한 것들을 기록
	* `H_t = O_1, R_1, A_1, ..., A_t−1, O_t, R_t`
	* Agent는 History를 보고 액션 결정
	* Environment는 History를 보고 Observation, Reward를 방출
* State : 다음에 무엇을 할지 결정하기 위해 쓰임
	* State는 History의 함수
	* `S_t = f(h_t)`

* Enviroment state
<img src='https://www.dropbox.com/s/7mzld3ahukklmfe/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2014.12.07.png?raw=1'>
	* `S_t^e` : 환경이 내적으로 갖고있는 표현
	* environment는 다음 observation / reward를 계산하는 것이 역할, 이때 observation / reward를 계산하는데 쓴 모든 것이 state
	* environment state는 보통 보이지 않음
	* Atari Example
		* environment : 게임
 		* observation : 게임 화면
 		* action : 조이스틱 컨트롤러
 		* reward : 게임 플레이 점수
 		* environment state : 게임이 액션을 받으면 다음 화면을 만들기 위해 몇 가지 숫자를 참조하여 다음 화면을 만듬(약 1400여개), 이 때 참조하는 숫자가 environment state
 	
* Agent State : 다음 액션을 취하는데 참조하는 state
<img src='https://www.dropbox.com/s/8p2nij63pujn5zd/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2014.26.40.png?raw=1'>
	* 주식을 하는데 어떤 주식에 투자하고자 할때 참고 하는 지표들, 거래량, 주가, 등
	* 그대로 쓸 수도 있고, 가공해서 쓸 수도 있음

* Information State
<img src='https://www.dropbox.com/s/bd1y4ztdxz0mp8p/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2014.34.41.png?raw=1'>
	* information state = markov state(중요) : 어떤 state가 markov한지 판단할 수 있음. 
	* 어떤 결정을 할 때 바로 이전 state만 참조하면 됨
	* `H_1:t -> S_t -> h_t+1:infinite`
	* 예시 : 헬리콥터를 조정하는데 현재 각도, 풍속, 등이 있을 때 추락시키지 않기 위해서는 10분 이전의 정보보다는 지금의 정보가 중요
	* `P[S_t+1|S_t]` 이 `S_1, .. , S_t` 가 다 제공된다 하더라도, `P[S_t+1|S_t]`가 성립되면 markov하다라고 판단할 수 있음

* Rat Example
	* state를 어떻게 정의하느냐에 따라 결과가 달라지게 됨
		* 개수를 세는걸로 state를 정하면? 치즈
		* 맨 마지막 시퀀스를 state로 하면? 감전
		* 모든 시퀀스를 state로 하면? 알수없음 

* Fully Observable Environments : environment state를 볼 수 있는 환경
<img src='https://www.dropbox.com/s/b7hg8fnvgtb9rng/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2014.47.55.png?raw=1'>
	* `O_t = S_t^a = S_t^e`
	* MDP(Markov Decision Process)라고 형식적으로 표현

* Partially Observable Environments : environment state를 볼 수 없는 환경
<img src='https://www.dropbox.com/s/bifwozmwwa2mba1/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2014.51.25.png?raw=1'>
	* agent state != environment state
	* POMDP(Partially Observable Markov Decision Process)라고 형식적으로 표현
	* 예시 : 로봇이 머리에 카메를 달고 움직일 경우
		* 로봇의 시야에 따라 위치 정보를 제공
		* 포커를 칠 때 상대의 패를 알 수 없음

## Agent 구성요소
### Policy, Value Function, Model : 3개를 모두 갖고 있을 수도 있고, 하나만 갖고 있을 수도 있음

* Policy : agent의 행동을 규정
	* state를 넣어주면 action을 return
	* 보통 π로 표시
	* Deterministic Policy : `a = π(s)` -> state를 넣어주면 action 하나가 결정
	* Stochastic Policy : -> state를 넣어주면 여러 action가 가능한대, 각 action의 확률을 return

* Value Function : 상황이 얼마나 좋은지를 나타냄
	* 게임이 끝날 때까지 미래 reward의 합산을 예측해 줌
	* `v_π(s) = E_π[R_t+1 + γR_t+2 + γ^2R_t+3 + ... | S_t = s]` -> state로부터 policy pi를 따라 갔을 때 게임이 끝날 때까지 얻을 reward의 기대값 

* Model : 환경이 어떻게 될지 예측
<img src='https://www.dropbox.com/s/uuinm7jhxsslbft/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2015.10.38.png?raw=1'>
	* reward를 예측 : state s에서 action a를 했을 때, reward를 뭘 받을지 r을 예측
	* state transition을 예측 : state s에서 action a를 했을 때, 다음 state s가 무엇이 될 지 예측

* Maze Example : Policy
	* Rewards : -1 per time-step
	* Actions : N, E, S, W
	* States : Agent`s location
	* Optimal Policy : Goal을 달성하기 위해 취해야하는 Action
	* Value Function : Optimal Policy를 따랐을 때 step별 reward 
	* Model : Agent가 생각하는 environment
		* transition model : P_ss`^a

## RL 분류
### RL Agnet 종류
<img src='https://www.dropbox.com/s/2aatgphxr0b8y52/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2015.18.13.png?raw=1'>

* Value Based : Value Function만 존재
	* No Policy (Implicit)
	* Value Function

* Policy Based : Policy만 존재
	* Policy
	* No Value Function

* Actor Critic
	* Policy
	* Value Function

* Model Free : Model을 만들지 않음
	* Policy and/or Value Function
	* No Model

* Model Based : environments model을 만듬
	* Policy and/or Value Function
	* Model

### 문제 분류
* Learning, Planning : 강화학습은 2가지를 포함
	* Reinforcement Learning = Learning
<img src='https://www.dropbox.com/s/xbmzoldk8axmrh8/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2015.26.46.png?raw=1'>
		* environments 모르는 상태에서 인터랙션을 하면서 policy를 개선해 나감
	* Planning = searching
<img src='https://www.dropbox.com/s/8u7zt8he6lzz5ry/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2015.27.07.png?raw=1'>
		* environments 아는 상태(reward, transition을 알고 있음)에서 실제로 environment를 하지 않고도 내부적으로 경쟁을 통해서, 딴 상황으로 갈 수가 있음 = 몬테카를로 서치(알파고와 같이)

### 관점
* Exploration : environments로부터 정보를 얻어서 environments 이해
	* 저녁을 먹을 때 새로운 식당을 가봄
	* 전혀 개발해서 석유가 많은 곳을 찾음

* Exploitation : environments로부터 정보를 바탕으로 최선의 선택을 하는 것
	* 저녁을 먹을 때 자주가던 식당에 감
	* 석유가 많은 곳을 알고 그곳을 개발

* Prediction : policy가 주어졌을 때 미래를 평가
<img src='https://www.dropbox.com/s/vhnp3n1w7hnhp1s/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2015.33.25.png?raw=1'>
	* value function 학습
	* action 한칸씩 이동 가능
	* random policy로 움직일 때 각 칸의 value는 얼마가 될까?

* Control : 미래를 최적화
<img src='https://www.dropbox.com/s/mg9aymh3nzde4ky/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-05%2015.33.46.png?raw=1'>
	* best policy를 찾음 
	* state에서 어떻게 움직여야 할지를 찾는 것

	
---
reference

* [팡요랩 : [강화학습 1강] 강화학습 introduction](https://www.youtube.com/watch?v=wYgyiCEkwC8)
* [RL Course by David Silver 강의 - Lecture 1](Introduction to Reinforcement Learning - https://www.youtube.com/watch?v=2pWv7GOvuf0)
* [RL Course by David Silver 교재 - Lecture 1](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/intro_RL.pdf)



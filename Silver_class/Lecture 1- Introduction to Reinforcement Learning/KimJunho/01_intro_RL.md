## Intro to RL

#### Reinforcement-Learning의 특징
- supervisor가 없고, reward signal만 존재.
- Feedback(reward) delay가 존재 --> reward가 즉각적으로 주어지지 않는다.(t+1 time step)
- sequential data여서 시간 순서가 중요.
- agent의 action에 따라 다음 데이터가 달라짐.


#### 용어
##### 1) Reward
- Scalar feedback signal --> reward의 총합을 최대로 만드는게 목적
- reward hypothesis를 잘 설정해야함
- 예를들어, '로봇이 잘 걷기위해선 서있을때 reward +1, 넘어지면 -100' 과 같이 reward hypothesis 설정이 중요

##### 2) Agent & Environment

# rl의 특징  
리워드만 있다  
지연된 리워드  
순서가 중요  

# Examples of rl  
### Fly stunt manoeuvres in a helicopter  
+ve reward for following desired trajectory ve reward for crashing  
### Defeat the world champion at Backgammon  
+/-ve reward for winning/losing a game  
### Manage an investment portfolio  
+ve reward for each $ in bank  
### Control a power station  
+ve reward for producing power  
-ve reward for exceeding safety thresholds  
### Make a humanoid robot walk  
+ve reward for forward motion  
-ve reward for falling over  
### Play many Atari games better than humans  
+/-ve reward for increasing/decreasing score 


# Reward  
스칼라  
목표: 누적 보상 최대화  
더 많은 리워드를 위해 즉각적인 리워드를 희생하는게 더 좋을 수도 있다  

# Agent와 Environment  
Agent가 a_t를 실행하면 Env는 o_t+1과 r_t+1을 준다  

# History와 State  
### History  
H_t = o_1, r_1, a_1, …, a_t-1, o_t, r_t (t까지의 모든 관측 가능한 변수)  
히스토리에 따라 다음 action, observation, reward가 달라짐  
### State  
S_t = f(H_t)  

# Environment State  
Environment state S_e,t는 Agent에게는 보이지 않고 observation과 reward를 결정하는데 쓰이는 environment 내부의 상태이다.  

# Agent State  
Agent State S_a,t는 action을 결정하는데 쓰이는 Agent의 상태이다.  
S_a,t = f(H_t)로 rl에서 쓰이는 정보다.  

# Markov  
P[s_t+1|s_t] = P[s_t+1|s_1,…,s_t] 일 때 s_t는 Markov라고 한다.  
Environment state와 history는 Markov하다.  

# Fully observable(MDP)  
Agent state == Environment state 일 때  

# Partially observable(POMDP)  
Agent state != Environment state 일 때  

# Policy  
s에서 a로의 함수  
### Deterministic Policy  
a = ㅠ(s)
### Stochastic Policy  
ㅠ(a|s) = P[A_t=a|S_t=s]  

# Value Function  
반환값의 기대값으로 state의 좋음/나쁨을 판별. 
v_ㅠ(s) = E[G_t|S_t=s]  

# Model  
Env가 다음에 할 행동을 예측하는게 Model  
P_ss’a = P[S_t+1=s’|S_t=s, A-t=a]  
R_sa = E[R_t+1|S_t=s, A_t=a]  
Agent가 가진 model은 대부분 불안전  
### Dynamics란?  
How actions change the state  

# RL Agent의 종류  
### Value Based  
Value Func 가지고 Policy를 구함  
### Policy Based  
직접 Policy를 구함  
### Actor-Critic  
위의 두 가지를 결합  
### Model Free
Model X
### Model Based
Model O

# Learning and Planning
### Learning
처음엔 환경을 모름  
환경과 상호작용하며 Policy를 발전시켜나감  
### Planning
처음부터 환경을 알고 계산을 통해 Policy를 발전시켜나감  
E.g. tree search  

# Exploit and Exploration
### Exploit
알고 있는 정보를 이용
### Exploration
새로운 정보를 얻기 위한 새로운 시도  

# Prediction and Control
### Prediction
가치 함수를 학습
### Control
가치 함수로 Policy를 구함  

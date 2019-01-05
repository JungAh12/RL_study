Lec 1 : Introduction to Reinforcement Learning

==============================================

About Reinforcement Learning

-------------------------------

강화학습의 특징
  * Supervisor 없이, 보상으로만 학습된다.
  * Feedback이 순간적이지 않고 지연된다.(미래의 Reward까지 계산)
  * Sequential이 중요하다.
  * Agent`s들의 action은 획득하는 미래의 데이터에 영향을 미친다.
    * 예를 들어, 로봇이 걸어가는 방향에 따라서 데이터가 매우 달라진다.
  
  
The Reinforcement Learning Problem

----------------------------------
Reward
  * Reward를 최대로 하는 것이 RL의 목표이다.
  * scalar feedback signal이다.
  * step t에서 agent가 얼마나 잘 action하는지를 보여준다.
  * agent들의 행동은 누적된 Reward가 Maximise한다.
  -> 지금 당장의 Reward보다 나중의 총 Reward가 maximise하는 방향이다.
   
   
뇌그림
Agent
  * 어떤 환경을 Observation하고, Reward를 받아서, Actions을 한다.
  * 여기서 Observation과 Reward와 Action을 하는 Environment가 존재한다.
   
   
History and State
  * History는 Observations, Actions, Rewards들이다.
  * State는 다음에 일어날 일을 결정하는 정보이다.
  * State는 History의 함수이다.
 
 
Environment State
  * Environment의 개인적인 정보이다.
  * Observation과 Reward를 선택하는데 사용됩니다.
  * Observation과 Reward만 제공하며 다른 정보들은 알지 못한다.
  * Agent들이 알지 못하며, 안다고 해도 관련된 정보를 가지고 있지 않는다.
 
 
Agent State
  * Agent State는 Environment State를 함축시킨 정보들을 획득하고,
  * 이를 토대로 Action을 취한다.

Information State
  * Information State(Markov State)는 History의 유용한 정보들을 함축하고 있다.
  * “The future is independent of the past given the present” 
  * 현재의 상태를 획득하면 과거 History들은 쓸모 없다.

Environment
  * Fully Observable Environments : Agent State와 Environment State와 Information State가 동일하다.(MDP)
    -> Own State를 Complete History, Baysian Distribution, RNN etc.. 으로 구축할 수 있다.
  * Partial Observable Environments : Agent State와 Environment State가 다르다.(POMDP)
  
Agent, Action(Joystick), Env(Game Machine), Observation(Game Screen), Reward( Score)

Inside An RL Agent
--------------------------------


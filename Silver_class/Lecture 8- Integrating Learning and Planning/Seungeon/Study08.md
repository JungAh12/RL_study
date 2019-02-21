# RL-study-2019
8장 까지는 MDP를 알 때 dynamic programming을 통해 문제를 푸는 방법도 배웠고, Model - free로 문제를 푸는 방법에 대해서도 배웠었다.

그래서 Prediction문제와 Control 문제를 푸는 법에 대해서 다루어 보았다.

또한 6강에서 Function approximation을 통해 문제를 scale-up하기도 해봤다ㅎㅎ

8장은 모델을 만들고, 모델을 기반으로 강화학습을 하는 문제! model을 알 때 푸는 것은 planning이고 model을 모를 때 푸는 것은 learning이라는 것을 기억하시고~~

이번 장에서는 planning과 learning을 섞는 법에 대해서도 조금 다룰 것입니다.

### Integrating Learning and Planning
바로 지난 강의에서는 경험으로부터 policy를 직접 학습했다.
그 이전의 강의에서는 value function을 경험으로 부터 직접 학습 했다.
이! 번! 엔! 경험들로 부터 model을 직접적으로 학습하는 것에 대해서 다룬다.

그 후에 모델을 통해서 value function과 policy를 constructing한다.
또한, learning과 planning을 single architecture에 integrate하는 것을 배운다.

#### Model-Free RL and Model-Based RL
Model - Free RL
  Model이 없다! 또한 경험으로 부터 Value function을 learning한다!

Model - Based RL
  경험으로 부터 model을 배운다
  model로 부터 value function 혹은 policy function을 planning한다!

#### Model-Based RL Reinforcement Learning
1. Model - based RL이란 policy가 action을 했을 때 생기는 경험을 통해서
2. model을 학습하고
3. Planning을 통해서 value와 policy를(MDP를) learn하고 solve 하는 것이다.

Advantages:
  Can efficiently learn model by supervised learning methods
  Can reason about model uncertainty
  1. spuervised learning을 통해서 model을 효율적으로 미리 학습 시킬 수 있다.
  2. 모델의 불확실성을 다룰 수 있다.

Disadvantages:
  First learn a model, then construct a value function
    => two suorces of approximation eror

























ㅇ

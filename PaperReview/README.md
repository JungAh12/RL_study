# Asynchronous Methods for Deep Reinforcement Learning

---

[TOC]

---

## [요약]

> *''비동기적 경사 하강법''을 이용한 심층강화학습 framework를 제안한다.*
> *이 경사하강법은 DNN controller 최적화를 위해 사용된다.*

- Neural Network Controller들을 위한 4가지 방법을 제시한다.
  - Asynchronous one-step Q-learning
  - Asynchronous one-step Sarsa
  - Asynchronous n-step Q-learning
  - Asynchronous advantage actor-critic
- 위 4가지 방법에 paraller actor-learner들을 사용했으며, training에 있어 안정화 효과가 있었다.
-  GPU 없이 multi-core CPU 만을 사용하고 절반의 시간동안 훈련하여, Atari game domain 의 SOTA를 넘어섰다.
- 다양한  continuous motor control 문제들과 navigating 문제를 visual input 을 이용하여 해결하였다.

## [동기]

Atari 2600과 같은 challenging domain들에서 experience replay에 기반한 Deep RL 알고리즘들은 놀라운 성과를 보여주었다.

- non-stationarity를 감소시켰다.
- update들을 decorrelate 시켰다.

하지만,

- real interaction 당 더 많은 메모리와 계산을 필요로 한다.
- older policy로부터 만들어진 data를 update할 수 있는 off-policy 알고리즘을 필요로 한다.

따라서, experience replay를 사용하는 대신 여러 agent들을,

- 비동기(asynchronously)
- 병렬(parallel)적으로

실행시키는 방법을 고안하였다.

## [주요 방법]

### 1. Asynchronous RL Framework

우리는  asynchronous actor-learner들을 사용하였다.

- single machine에 multiple CPU thread들을 사용하였다.
- single machine에서 사용하므로써, gradient와 parameter들 전송에 필요한 communication cost들을 제거했다.

또한, multiple actors-learner들을 병렬적으로 실행시킴으로써,

- 환경의 다양한 부분들을 탐험할 수 있도록 하였다.
- 각각의 actor-leaner마다 다른 exploration policy들을 사용할 수 있어, diversity를 최대화할 수 있었다.

다른 thread들에서 exploration policy들을 실행시킴으로써 parameter들이 덜 correlated되도록 하였다.

training time이, actor-learner 수에 비례하여 감소하였다.

on-policy method들을 안정적으로 사용할 수 있게 되었다.
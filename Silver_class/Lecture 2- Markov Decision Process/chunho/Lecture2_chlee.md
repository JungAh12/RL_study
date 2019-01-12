# RL Course by David Silver - Lecture 2: Markov Decision Processes


## Markov Processes
### MDPs 소개
* MDP는 RL에서 environment를 formally describe함
* MDP는 fully observable Environments 할 수 있는 곳
* 즉, 현재 상태는 프로세스의 특성을 완전히 나타냄
* 거의 모든 RL 문제를 MDPs formalised함
* 예시
	* Optimal control
	* Partially observable problems
	* Bandits : 카지노 슬롯머신

### Markov Property
<img src='https://www.dropbox.com/s/clrsbizeheuurau/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.29.51.png?raw=1'>

* `S_t에서 S_t+1로 갈 수 있는 확률이 S_1, ..., S_t를 다 주어졌을때와 같다.` -> 이전 과거를 다 버릴 수 있다.
* state가 모든 관련된 정보를 갖고 있어서, state만 필요할 뿐 history는 필요하지 않음
* state는 미래에 대한 충분한 통계적 표현형

### State Transition Matrix
<img src='https://www.dropbox.com/s/kkodme2y2ez27i6/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.29.47.png?raw=1'>

* Markov Process, Markov Reward Process, Markov Decision Process 모두 쓰이는 개념
* `시간 t일 때, s에 있다면, Markov process에서는 action 없고 매 step마다 정해진 확률로 다음 state로 옮겨다님 -> t에 있을 때, t+1이 될 수 있는 state가 여러개 있는데 각 state로 전이 할 수 있는 확률`
* 위의 식으로 표현하면, **State Transition Probability**
* 아래의 매트릭스로 표현하면, **State Transition Matrix**

### 문제 셋팅 : Markov Process
<img src='https://www.dropbox.com/s/wrjiktoe59yuxrb/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.30.01.png?raw=1'>

* State들이 n개가 있고, descript하게 상태가 끊겨서 있는 상태
* S와 P만 있으면 정의됨
* S : State의 유한한 set
* P : State Transition Probability Matrix -> n x n matrix
* n 제곱개의 숫자들과 n개의 state가 있으면 Markov Process는 완전히 정의가 됨 = **Markov Train**이라고도 함
* memoryless random process = 어느 경로로 현재 state 온 것과 상관없이 현재 state로 오면 미래가 정해졌다는 것 = Markov Propoty
* random process = 샘플링을 할 수 있음

# Example : Student Markov Chain Episodes
<img src='https://www.dropbox.com/s/owv7dz8l52sksek/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.30.20.png?raw=1'>

* state : 7개
* state 전이 확률은 화살표로 표현
* 터미널 state : 마지막 state로 1.0으로 진행되는 화살표
* episodes : 어느 state로 시작해서 터미널 state까지 이동한 것
* episodes sampling : 시뮬레이션한 케이스
	* C1 C2 C3 Pass Sleep
	* C1 FB FB C1 C2 Sleep
	* C1 C2 C3 Pub C2 C3 Pass Sleep
	* C1 FB FB C1 C2 C3 Pub C1 FB ... C2 Sleep

<img src='https://www.dropbox.com/s/l9gj34hnb1sb9cb/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.30.24.png?raw=1'>

* State Transition Matrix로 정의한 경우

## Markov Reward Processes
<img src='https://www.dropbox.com/s/2vk46xm95f1bpgl/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.30.31.png?raw=1'>

* S : State의 유한한 set
* P : State Transition Probility Matrix
* R : Reward 함수 = state별로 정의, n개 존재
* γ(gamma) : discount factor

### Example : Student MRP
<img src='https://www.dropbox.com/s/m6mpexqt45u6qfn/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.30.40.png?raw=1'>

* state마다 Reward가 존재

### Return
<img src='https://www.dropbox.com/s/13keka76ly0fd99/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.30.46.png?raw=1'>

* 강화학습은 Return을 maximizer 하는 것
* Reworad와 Return은 다름
* gamma가 0에 가까우면 순간적인(**myopic**) reward가 중시, 1에 가까울수록 전체적인 reward(**far-sighted**)가 중시

<img src='https://www.dropbox.com/s/hocr0bkp6thrnf9/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.30.51.png?raw=1'>

* 수학적으로 편리해서 discount를 사용 (솔직한 정의)
* 동물과 사람의 행동이 즉각적인 행동을 선호함
* 만약에 모든 state가 터미널 state로 이동하는게 보장된다면, gamma가 1로 가도 됨

### Value Function
<img src='https://www.dropbox.com/s/5vsj5i4bso9adx7/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.31.02.png?raw=1'>

* Value Function : Return의 기대값
* G : State s에 왔을 때 조건부 G의 기대값 C Value Function
* `G_t`는 확률변수

<img src='https://www.dropbox.com/s/c3oj38l9p680i8y/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.31.09.png?raw=1'>

* 에피소드별 return 값
	* -2.25 = C1 C2 C3 Pass Sleep
	* -3.125 = C1 FB FB C1 C2 Sleep
	* -3.41 = C1 C2 C3 Pub C2 C3 Pass Sleep
	* -3.20 = C1 FB FB C1 C2 C3 Pub C1 FB ... C2 Sleep
* 에피소드별 return값을 평균 내면, C1에 왔을 때 어느정도의 return 받을 수 있다고, 기대값을 정의할 수 있음 

### value는 구하는 방법
<img src='https://www.dropbox.com/s/syg7e7v6p1jj093/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.31.17.png?raw=1'>

* gamma = 0

<img src='https://www.dropbox.com/s/5gcbc6ptyegoj06/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.31.27.png?raw=1'>

* gamma = 0.9

<img src='https://www.dropbox.com/s/ueb27m9e0izagd7/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.31.33.png?raw=1'>

* gamma = 1

### Bellman Equation(**매우중요**)
<img src='https://www.dropbox.com/s/jonqv0j6o2jvskn/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.31.42.png?raw=1'>

* 

<img src='https://www.dropbox.com/s/7s18smkvvf64ais/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.31.50.png?raw=1'>

<img src='https://www.dropbox.com/s/t9bs6vxcurcakyw/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.31.58.png?raw=1'>

<img src='https://www.dropbox.com/s/8txkejah2dygvh8/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.32.02.png?raw=1'>

<img src='https://www.dropbox.com/s/nhea02ff62yoj7i/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.32.11.png?raw=1'>

---
## Markov Decision Processes

<img src='https://www.dropbox.com/s/qjflw5ek5am9m93/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.32.18.png?raw=1'>

<img src='https://www.dropbox.com/s/vwyc16j4owu3kjl/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.32.24.png?raw=1'>

<img src='https://www.dropbox.com/s/og88dvugm0whm47/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.32.33.png?raw=1'>

<img src='https://www.dropbox.com/s/wew0efr5f0okt51/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.32.53.png?raw=1'>

<img src='https://www.dropbox.com/s/akqi1nnhsdradss/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.33.00.png?raw=1'>

<img src='https://www.dropbox.com/s/zc5nfocrbptv5ac/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.33.08.png?raw=1'>

<img src='https://www.dropbox.com/s/2y9jhnizufp3lmq/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.33.15.png?raw=1'>

<img src='https://www.dropbox.com/s/pgwpu8ckpsewbhp/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.33.25.png?raw=1'>

<img src='https://www.dropbox.com/s/kacvutfz91ip43d/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.33.32.png?raw=1'>

<img src='https://www.dropbox.com/s/nlukurx6x4zum01/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.33.38.png?raw=1'>

<img src='https://www.dropbox.com/s/zy9649ezu6bhs68/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.36.15.png?raw=1'>

<img src='https://www.dropbox.com/s/9scyl41vrtu20kc/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.36.22.png?raw=1'>

<img src='https://www.dropbox.com/s/x53wpo9wl2xjkot/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.36.53.png?raw=1'>

<img src='https://www.dropbox.com/s/08cwmh1tf6e1k6a/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.37.03.png?raw=1'>

<img src='https://www.dropbox.com/s/z1guddhlhaf3q3g/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.37.12.png?raw=1'>

<img src='https://www.dropbox.com/s/lz6vuxq3eoseiux/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.37.23.png?raw=1'>

<img src='https://www.dropbox.com/s/0irafiapj3v7gks/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.37.27.png?raw=1'>

<img src='https://www.dropbox.com/s/e5c7e4h8e4uo6wf/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.37.34.png?raw=1'>

---
## Extensions to MDPs

<img src='https://www.dropbox.com/s/jetkxyle31dk7jw/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.37.42.png?raw=1'>

<img src='https://www.dropbox.com/s/p81rum2neho3btg/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.37.48.png?raw=1'>


<img src='https://www.dropbox.com/s/q87lda5bse138n1/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.37.54.png?raw=1'>

<img src='https://www.dropbox.com/s/mry77xazhcaj6xu/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.37.58.png?raw=1'>

<img src='https://www.dropbox.com/s/texr0v2d8x3gyv7/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.38.02.png?raw=1'>

<img src='https://www.dropbox.com/s/24clhcl6ejxqutq/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.38.06.png?raw=1'>

<img src='https://www.dropbox.com/s/24clhcl6ejxqutq/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.38.06.png?raw=1'>

<img src='https://www.dropbox.com/s/29ob7xsie8d022d/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.38.12.png?raw=1'>

<img src='https://www.dropbox.com/s/le0u2uw5bmj5v87/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.38.18.png?raw=1'>

<img src='https://www.dropbox.com/s/07lqhrst8lcj6x8/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202019-01-12%2015.38.26.png?raw=1'>


	
---
reference

* [팡요랩 : [강화학습 2강] Markov Decision Process
](https://www.youtube.com/watch?v=NMesGSXr8H4)
* [RL Course by David Silver - Lecture 2: Markov Decision Process
](https://www.youtube.com/watch?v=lfHX2hHRMVQ)
* [RL Course by David Silver 교재 - Lecture 2](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/MDP.pdf)


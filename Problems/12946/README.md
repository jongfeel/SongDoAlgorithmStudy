# Problem 12946

## 하노이의 탑

### 문제 설명

하노이 탑(Tower of Hanoi)은 퍼즐의 일종입니다. 세 개의 기둥과 이 기동에 꽂을 수 있는 크기가 다양한 원판들이 있고, 퍼즐을 시작하기 전에는 한 기둥에 원판들이 작은 것이 위에 있도록 순서대로 쌓여 있습니다. 게임의 목적은 다음 두 가지 조건을 만족시키면서, 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것입니다.

1. 한 번에 하나의 원판만 옮길 수 있습니다.
2. 큰 원판이 작은 원판 위에 있어서는 안됩니다.

하노이 탑의 세 개의 기둥을 왼쪽 부터 1번, 2번, 3번이라고 하겠습니다. 1번에는 n개의 원판이 있고 이 n개의 원판을 3번 원판으로 최소 횟수로 옮기려고 합니다.

1번 기둥에 있는 원판의 개수 n이 매개변수로 주어질 때, n개의 원판을 3번 원판으로 최소로 옮기는 방법을 return하는 solution를 완성해주세요.

### 제한사항

- n은 15이하의 자연수 입니다.

### 입출력 예

|n|result|
|-|------|
|2|[[1,2], [1,3], [2,3]]|

### 입출력 예 설명

입출력 예 #1

다음과 같이 옮길 수 있습니다.

![https://i.imgur.com/SWEqD08.png](https://i.imgur.com/SWEqD08.png)
![https://i.imgur.com/mrmOzV2.png](https://i.imgur.com/mrmOzV2.png)
![https://i.imgur.com/Ent83gA.png](https://i.imgur.com/Ent83gA.png)
![https://i.imgur.com/osJFfhF.png](https://i.imgur.com/osJFfhF.png)

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12946?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12946?language=python3)

## System Requirement

- Tool: Visual Studio Code
- SDK: Python 3.7.2
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "12946" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 하노이의 탑은 워낙에 유명한 문제다 보니 이미 잘 알려진 recursive function을 잘 사용하면 풀 수 있다. 솔직히 recursive에 대한 개념만 이해 되면 그냥 풀 수 있다.
- 그런데 나는 어떤 규칙성을 찾고 거기서 뭔가 방법을 찾고 싶어서 아래 구글 스프레드시트와 같은 방법으로 풀어서 해석해봤는데
- [https://docs.google.com/spreadsheets/d/1oECL7h3iNBc7BebUUxPI1CQ3c3_v1Ir0IYlpr4EvDxs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1oECL7h3iNBc7BebUUxPI1CQ3c3_v1Ir0IYlpr4EvDxs/edit?usp=sharing)
- 이 방법이 recursive한 방법을 풀어 놓은거 정도 밖에 안되서 그냥 recursive function 기법으로 함
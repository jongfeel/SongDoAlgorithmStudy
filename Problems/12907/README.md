# Problem 12907

## 거스름돈

### 문제 설명

Finn은 편의점에서 야간 아르바이트를 하고 있습니다. 야간에 손님이 너무 없어 심심한 Finn은 손님들께 거스름돈을 n 원을 줄 때 방법의 경우의 수를 구하기로 하였습니다.

예를 들어서 손님께 5원을 거슬러 줘야 하고 1원, 2원, 5원이 있다면 다음과 같이 4가지 방법으로 5원을 거슬러 줄 수 있습니다.

- 1원을 5개 사용해서 거슬러 준다.
- 1원을 3개 사용하고, 2원을 1개 사용해서 거슬러 준다.
- 1원을 1개 사용하고, 2원을 2개 사용해서 거슬러 준다.
- 5원을 1개 사용해서 거슬러 준다.

거슬러 줘야 하는 금액 n과 Finn이 현재 보유하고 있는 돈의 종류 money가 매개변수로 주어질 때, Finn이 n 원을 거슬러 줄 방법의 수를 return 하도록 solution 함수를 완성해 주세요.

### 제한사항

- n은 100,000 이하의 자연수입니다.
- 화폐 단위는 100종류 이하입니다.
- 모든 화폐는 무한하게 있다고 가정합니다.
- 정답이 커질 수 있으니, 1,000,000,007로 나눈 나머지를 return 해주세요.

### 입출력 예

|n|money|result|
|-|-----|------|
|5|[1, 2, 5]|4|

### 입출력 예 설명

입출력 예 #1
문제의 예시와 같습니다.

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12907?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12907?language=python3)

## System Requirement

- Tool: Visual Studio Code
- SDK: Python 3.7.2
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "12907" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 전형적인 DP 문제이자, array에서 내 이전 index가 의미하는게 뭔지만 알면 되는 문제
- 한 동전의 가치로 n 원을 거슬러 줄 수 있는 방법의 수를 차례로 기억한다.
  - 여기에서의 예로는 1원으로 1원을 거슬러 줄 수 있는 방법 1가지
  - 1원으로 2원을 거슬러 줄 수 있는 방법 1가지 ...
- 또 그 다음 동전의 가치로 n 원을 거슬러 줄 수 있는 방법의 수를 또 차례로 기억한다.
  - 2원으로는 1원어치를 거슬러 줄 수 없으므로 방법 0가지
  - 2원으로 2원어치를 거슬러 줄 수 있는 방법 1가지, 그런데 1원으로 2원어치를 거슬러 줄 수 있는 방법이 있으므로 합하면 2가지
  - 2원으로 3원어치를 거슬러 줄 수 있는 방법 0가지, 그런데 1원으로 3원어치를 거슬러 줄 수 있는 방법까지 합하면 1가지가 된다. 게다가 2원을 제외하고 남은 1원은 거슬러 줄 수 있는 방법을 1원으로 1원어치 거슬러 줄 수 있는 방법이 있으므로 1가지를 더 추가하면 총 2가지가 된다.
  - 나머지는 계속 탐색해 나가다 보면 방법의 가지수를 쭉 더해 나가면서 찾아볼 수 있다.
- 아래 google spreadsheet를 살펴보면 조금 이해가 될 것이다.
  - [https://docs.google.com/spreadsheets/d/1wbtqMzviAA1384QV9VQO36MwM-kTQ-2x46mbAiH3imI/edit#gid=0](https://docs.google.com/spreadsheets/d/1wbtqMzviAA1384QV9VQO36MwM-kTQ-2x46mbAiH3imI/edit#gid=0)
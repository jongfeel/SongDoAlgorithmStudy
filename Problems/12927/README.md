# Problem 12927

## 야근 지수

### 문제 설명

회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다. 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

### 제한 사항

- works는 길이 1 이상, 20,000 이하인 배열입니다.
- works의 원소는 50000 이하인 자연수입니다.
- n은 1,000,000 이하인 자연수입니다.

### 입출력 예

|works|n|result|
|-----|-|------|
|[4,3,3]|4|12|
|[2,1,2]|1|6|
|[1,1]|3|0|

### 입출력 예 설명

입출력 예 #1\
n=4 일 때, 남은 일의 작업량이 [4, 3, 3] 이라면 야근 지수를 최소화하기 위해 4시간동안 일을 한 결과는 [2, 2, 2]입니다. 이 때 야근 지수는 22 + 22 + 22 = 12 입니다.

입출력 예 #2\
n=1일 때, 남은 일의 작업량이 [2,1,2]라면 야근 지수를 최소화하기 위해 1시간동안 일을 한 결과는 [1,1,2]입니다. 야근지수는 12 + 12 + 22 = 6입니다.

입출력 예 #3

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12927?language=java](hhttps://programmers.co.kr/learn/courses/30/lessons/12927?language=java)

## System Requirement

- Tool: Visual Studio Code
- SDK: Java SDK 1.8.0_161-b12
- Language: Java

## Test - bash

```bash
javac Problem.java
```

```bash
java Problem
```

## Test - Visaul Studio Code

- Open folder "12927" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 작업량 배열의 숫자들이 작으면 적을 수록 피로도 계산을 할 때 가장 피로도를 최소화 할 수 있다.
- 그러므로 항상 작업량이 큰 숫자 부터 구해와서 작업량을 줄여 나가야 하는 문제
- python에서 heapq에 재미를 본 바 이번 문제도 java의 priority queue를 이용해서 배열에서 가장 큰 수를 빨리 구하는 자료구조를 사용
- 피로도 계산은 어렵지 않으니 재미있는 java의 stream을 이용한 코딩을 진행해서 네 줄로 끝내본다.
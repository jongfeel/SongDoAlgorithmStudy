# Problem 12900

## 2 x n 타일링

### 문제 설명

가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

- 타일을 가로로 배치 하는 경우
- 타일을 세로로 배치 하는 경우

예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.

![https://i.imgur.com/29ANX0f.png](https://i.imgur.com/29ANX0f.png)

직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.

### 제한사항

- 가로의 길이 n은 60,000이하의 자연수 입니다.
- 경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.

### 입출력 예

|n|result|
|--|------|
|4|5|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12900?language=javascript](https://programmers.co.kr/learn/courses/30/lessons/12900?language=javascript)

## System Requirement

- Tool: Visual Studio Code
- Language: javascript

## Test - bash

```bash
node Problem.js
```

## Test - Visaul Studio Code

- Open folder "Problem/12900" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 흔한 DP (Dynamic Programming) 문제
- n=1, n=2, n=3, n=4, n=5, ... 일 때의 경우의 수를 차례로 구해보면
- 1, 2, 3, 5, 8, ... 이 되고 규칙을 찾아 보면 현재 경우의 수는 앞의 경우의 수와 앞앞의 경우의 수의 합이 되는 걸 발견할 수 있다. Fibonacci 수열.
- 로직 자체는 단순하니 보고 이해하면 되고
- DP가 어떤 건지 잘 이해를 하는게 중요할 듯.
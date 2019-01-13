# Problem 12914

## 멀리 뛰기

### 문제 설명

효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는\
(1칸, 1칸, 1칸, 1칸)\
(1칸, 2칸, 1칸)\
(1칸, 1칸, 2칸)\
(2칸, 1칸, 1칸)\
(2칸, 2칸)\
의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

### 제한 사항

- n은 1 이상, 2000 이하인 정수입니다.

### 입출력 예

|n|result|
|-|------|
|4|5|
|3|3|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12914?language=javascript](https://programmers.co.kr/learn/courses/30/lessons/12914?language=javascript)

## System Requirement

- Tool: Visual Studio Code
- Language: javascript

## Test - bash

```bash
node Problem.js
```

## Test - Visaul Studio Code

- Open folder "12914" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 경우의 수를 구하다 보니 또 Fibonacci 수열, 또 DP 문제
- [12900](https://github.com/jongfeel/SongDoAlgorithmStudy/tree/master/Problems/12900) 문제와 놀랍도록 똑같다.
- 유일하게 다른 점 하나라면 숫자가 커지는 것에 대비해 특정 수의 나머지를 구하는 건데, 이 문제에서는 1234567이다.
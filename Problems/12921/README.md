# Problem 12921

## 소수 찾기

### 문제 설명

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

### 제한 조건

- n은 2이상 1000000이하의 자연수입니다.

### 입출력 예

|n|result|
|-|------|
|10|4|
|5|3|

### 입출력 예 설명

입출력 예 #1\
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2\
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12921?language=java](hhttps://programmers.co.kr/learn/courses/30/lessons/12921?language=java)

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

- Open folder "12921" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 제한 조건이 크기 때문에 for문 두번 써서 구하는 방법으로는 되지 않는다.
- 에라토스테네스의 체를 이용한 방법을 알고 있었으므로 그 방식으로 구현한다.
  - 어떤 수가 소수인지를 판별하려면 그 수의 sqrt 까지의 수 만큼만 조사해도 된다.
  - 어떤 수가 소수가 아니라고 판단되면 그 double에 해당하는 수도 소수가 아니게 된다.
  - 예1) 2, 4, 6, 8, 10, ...
  - 예2) 3, 6, 9, 12, 15, ...
- 최종적으로 소수가 아닌 수를 걸러내면 남아 있는 수는 소수인 수가 되며 그 갯수를 체크하는 for문을 한번 더 돌면 값을 구할 수 있다.
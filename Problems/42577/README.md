# Problem 42577

## 전화번호 목록

### 문제 설명

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.

### 입출력 예

|phone_book|return|
|--|------|
|["119", "97674223", "1195524421"]|false
|["123", "456", "789"]|true
|["12", "123", "1235", "567", "88"]|false

### 문제 링크 

[https://programmers.co.kr/learn/courses/30/lessons/42577?language=java](hhttps://programmers.co.kr/learn/courses/30/lessons/42577?language=java)

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

- Open folder "42577" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 문제를 보자마자 떠오른 String method인 startsWith 이거 하나면 이 문제를 다 푼거나 다름 없다.
- 최대 1,000,000의 for문을 중첩으로 두 번 돌아서 O(n<sup>2</sup>)의 복잡도를 가지기에 만약에 효율성 테스트에서 통과 안되면 다른 언어 써야지... 했는데, 의외로 통과됨
- 알고리즘 자체는 간단한데
  - index 0 부터 해서 두번 중첩 for 문을 돌려준다.
  - 자기 자신은 비교할 필요가 없으므로 continue로 넘어감
  - 접두어(prefix)로 선정된 번호가 나머지 번호의 처음과 일치하는지 비교
  - 일치하는 번호 발견하면 바로 return false
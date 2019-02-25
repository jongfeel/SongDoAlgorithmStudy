# Problem 12904

## 가장 긴 팰린드롬

### 문제 설명

앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

예를들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.

### 제한사항

- 문자열 s의 길이 : 2500 이하의 자연수
- 문자열 s는 알파벳 소문자로만 구성

### 입출력 예

|s|answer|
|-|------|
|"abcdcba"|7|
|"abacde"|3|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12904?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12904?language=python3)

## System Requirement

- Tool: Visual Studio Code
- SDK: Python 3.7.2
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "12904" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- brute force 작전으로 간다.
- 가장 긴 palinedrome을 구하는 것이므로 전체 string length 만큼의 string과 reverse된 string이 같은지 비교한다.
  - 여기서 비교는 한번만 이루어진다.
  - 맞으면 length를 return 한다.
- 그 다음은 length - 1 만큼의 길이가 되는 string과 reverse된 string이 같은지 비교한다.
  - 여기서는 아래 두 개의 패턴의 string을 구할 수 있다.
    - 0 to length-1
    - 1 to length
  - 예제 2번으로 얘기하자면 "abacde"에서
    - "**abacd**e"
    - "a**bacde**"
    - 위 bold된 두 string을 구할 수 있다.
  - 그리고 bold된 string과 reverse된 string이 같은지 비교한다.
  - 맞으면 length-1을 리턴한다. 하지만 palindrome이 아니다.
- 그 다음은 length - 2 만큼의 string과 reverse된 string이 같은지 비교한다.
  - 마찬가지로 length - 2가 되었으므로 아래의 세 개의 패턴의 string을 구할 수 있다.
    - 0 to length-2
    - 1 to length-1
    - 2 to length
  - 예제 2번으로 얘기하면 "abacde"에서
    - "**abac**de"
    - "a**bacd**e"
    - "ab**acde**"
  - 위 bold된 세 string을 구할 수 있다.
- 이런 식으로 length-n을 길이만큼의 string과 reverse string을 구해 비교해 나가면 가장 긴 palindrome를 구해 나가는 방법을 만들 수 있다.
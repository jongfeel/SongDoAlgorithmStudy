# Problem 12924

## 숫자의 표현

### 문제 설명

Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

- 1 + 2 + 3 + 4 + 5 = 15
- 4 + 5 + 6 = 15
- 7 + 8 = 15
- 15 = 15

자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

### 제한사항

- n은 10,000 이하의 자연수 입니다.

### 입출력 예

|n|result|
|-|------|
|15|4|

### 입출력 예 설명

입출력 예 #1
문제의 예시와 같습니다.

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12924?language=cpp](https://programmers.co.kr/learn/courses/30/lessons/12924?language=cpp)

## System Requirement

- Tool: Visual Studio Code
- Language: C++
- Compiler: g++.exe (MinGW.org GCC-6.3.0-1) 6.3.0
- Use MinGW

## MinGW Download (only windows)

- [https://sourceforge.net/projects/mingw/files/](https://sourceforge.net/projects/mingw/files/)

## Test - bash

Change directory git root: /12924
and compile

```bash
g++ -static Problem.cpp
```

[with debugging](https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html#Debugging-Options)

```bash
g++ -static -g Problem.cpp
```

> Windows Environment Settings
> System Variable > Path > Add "C:\MinGW\bin" (Installed path)

Run

```bash
a
```

## Test - Visaul Studio Code

- Open folder "12924" by Visual Studio Code
- Check out settings: launch.json and tasks.json
  - launch.json
    - "miDebuggerPath": "C:/mingw/bin/gdb.exe"
    - Use MinGW installed your path
  - tasks.json
    - Use gdb debug: args[0] = "-g"
- Press F5 to debug start

## Solve

- 주어진 조건을 잘 보고 이해하면 좋을 것 같다.
- n이 10,000까지여서 얼핏 O(n^2)의 시간복잡도 즉 100,000,000(1억) 번 까지 돌거 같은데 사실 그렇게 될 일이 없다.
  - 1부터 차례대로 찾기 시작해서 끝까지 돌면 그럴 거 같지만
  - 만약 n이 100 이라고 하면 loop index 50부터는 의미가 없어진다.
  - 이유는 50 + 51 만 진행해도 100이 넘기 때문에 저절로 안쪽의 loop는 sum > n 보다 큰 조건을 만족해서 break가 걸린다.
- 그런 이유로 brute force로 1부터 n까지 쭉 돌려 가면서 sum == n이 되는 조건을 찾아 나간다.
- c++로 짜면 정확성은 물론이고 효율성 테스트까지 0.05ms 내에 답을 구할 수 있다.
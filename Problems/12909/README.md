# Problem 12909

## 올바른 괄호

### 문제 설명

올바른 괄호란 두 개의 괄호 '(' 와 ')' 만으로 구성되어 있고, 괄호가 올바르게 짝지어진 문자열입니다. 괄호가 올바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 합니다.
예를들어

- ()() 또는 (())() 는 올바른 괄호입니다.
- )()( 또는 (()( 는 올바르지 않은 괄호입니다.

'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return하는 solution 함수를 완성해 주세요.

### 제한사항

- 문자열 s의 길이 : 100,000 이하의 자연수
- 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

### 입출력 예

|s|answer|
|-|------|
|"()()"|true|
|"(())()"|true|
|")()("|false|
|"(()("|false|

### 입출력 예 설명

입출력 예 #1,2,3,4
문제의 예시와 같습니다.

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12909?language=cpp](https://programmers.co.kr/learn/courses/30/lessons/12909?language=cpp)

## System Requirement

- Tool: Visual Studio Code
- Language: C++
- Compiler: g++.exe (MinGW.org GCC-6.3.0-1) 6.3.0
- Use MinGW

## MinGW Download (only windows)

- [https://sourceforge.net/projects/mingw/files/](https://sourceforge.net/projects/mingw/files/)

## Test - bash

Change directory git root: /12909
and compile

```bash
g++ Problem.cpp
```

[with debugging](https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html#Debugging-Options)

```bash
g++ -g Problem.cpp
```

> Windows Environment Settings
> System Variable > Path > Add "C:\MinGW\bin" (Installed path)

Run

```bash
a
```

## Test - Visaul Studio Code

- Open folder "12909" by Visual Studio Code
- Check out settings: launch.json and tasks.json
  - launch.json
    - "miDebuggerPath": "C:/mingw/bin/gdb.exe"
    - Use MinGW installed your path
  - tasks.json
    - Use gdb debug: args[0] = "-g"
- Press F5 to debug start

## Solve

- 아주 쉽게 string의 각 index 별로 loop를 돌면서 "(" 이면 +1, ")"이면 -1로 계산하면 checkPair 값이 최종적으로 0이 됐을 때가 괄호 쌍이 맞으므로 true 아니면 false를 return
- 그런데 테스트 3번의 경우가 실패
  - 잘 보면 +2, -2로 0이 되긴 하는데 열고 닫는 쌍으로는 맞지 않아 true로 계산이 되므로
  - 괄호가 마이너스(-)가 되는 순간은 괄호 쌍이 안맞아 그냥 false를 return 하는게 맞겠다 싶어 추가 수정
- 그리고 채점해 보면 효율성 테스트 까지 통과함
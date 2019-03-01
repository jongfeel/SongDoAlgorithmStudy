# Problem 12973

## 짝지어 제거하기

### 문제 설명

짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

### 제한사항

- 문자열의 길이 : 1,000,000이하의 자연수
- 문자열은 모두 소문자로 이루어져 있습니다.

### 입출력 예

|s|result|
|-|------|
|baabaa|1|
|cdcd|0|

### 입출력 예 설명

입출력 예 #1\
위의 예시와 같습니다.\
입출력 예 #2\
문자열이 남아있지만 짝지어 제거할 수 있는 문자열이 더 이상 존재하지 않기 때문에 0을 반환합니다.

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12973?language=javascript](https://programmers.co.kr/learn/courses/30/lessons/12973?language=javascript)

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

- 처음엔 string index 만큼 돌면서 index == index+1의 값이 같으면 삭제하는 식으로 하려고 했다.
- 그런데 그렇게 하면 length가 동적으로 바뀌게 되므로 주어진 s.length 만큼의 for loop index 연산에 언젠가 오류가 나게 되어 있다.
- 다시 자세히 보면 연속된 글자의 값이 같을 때만 삭제하는 조건이므로 index 연산까지 할 필요가 없다는 점에 착안, stack을 사용한다.
  - 현재 stack.top의 글자가 지금 넣으려는 글자와 같은지 비교한다.
  - 같으면 stack.pop을 하고
  - 다르면 stack.push를 진행한다.
  - pop을 하는 이유는 연속된 같은 글자이고 이미 들어가 있는 글자를 지우면 같은 글자를 지우는 효과를 얻을 수 있기 때문이다.
- 이렇게 하면 index 계산을 하지 않고도 답을 구할 수 있다.
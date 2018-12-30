# Problem 12951

## JadenCase 문자열 만들기

### 문제 설명

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

### 제한 조건

- s는 길이 1 이상인 문자열입니다.
- s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
- 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )

### 입출력 예

|s|return|
|-|------|
|"3people unFollowed me"|"3people Unfollowed Me"|
|"for the last week"|"For The Last Week"|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3)

## System Requirement

- Tool: Visual Studio Code
- Extension: Python extension for Visual Studio Code, Python 3.6.5
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "12951" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- Python에 title() 이라는 함수를 알고 있었기 때문에 python을 사용함
  - title(): 어떤 문자열 중 첫 글자를 대문자로 변환, 단어 단위로 변환해 줌
  - 문제 조건 중에 첫 자리가 숫자도 있다는 게 없었으면 아래 한줄로 문제가 끝날 수도 있었음
  - return s.title()
- 그런데 문제에 함정이 있음
  - 조건이 알파벳과 공백문자로만 이루어져 있다고 했는데 그 공백이 순수하게 " " 1 space가 아닐 수 있다는 거 정도이다.
  - 실제로 공백이 두 개 이상 있는 문자열을 split(" ")으로 해보면 공백도 하나의 array index로 들어가기 때문에 처리를 해 줘야 함
  - 예) "h e  l   l    o".split(" ") => ['h', '', 'e', '', '', 'l', '', '', '', 'l', '', '', '', '', 'o']
- 문제에 함정이 또 있음
  - 문장 사이의 공백의 갯수는 허용해야 하지만 문장의 뒤에 있는 공백은 무시해야 함
  - 코드 로직 상 마지막 문장에 " " 공백이 들어가므로 [:-1]을 해서 공백 제거 필요
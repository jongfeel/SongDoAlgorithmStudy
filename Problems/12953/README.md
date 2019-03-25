# Problem 12953

## N개의 최소공배수

### 문제 설명

두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

### 제한사항

- arr은 길이 1이상, 15이하인 배열입니다.
- arr의 원소는 100 이하인 자연수입니다.

### 입출력 예

|arr|result|
|---|------|
|[2, 6, 8, 14]|168|
|[1, 2, 3]|6|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3)

## System Requirement

- Tool: Visual Studio Code
- SDK: Python 3.7.2
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "42886" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 최소공배수 LCM(Least Common Multiple)과 최대공약수 GCD(Greatest Common Divisor)구하는 함수는 흔하므로
- arr를 어떻게 처리해서 LCM을 구할 수 있는지에 집중한다.
- 참고로 LCM을 구하려면 GCD를 필연적으로 구해야 한다.
- 각각 두 수의 LCM을 구한 수를 또 다른 수와 계속해서 LCM을 구해 나가면 결국엔 모든 수들의 LCM을 구할 수 있다는게 포인트이므로
- C#의 Aggregation, javascript의 reduce가 번뜩 떠오르게 되어있다.
- Python에도 reduce 함수가 있으니 적극 활용하면 답을 구할 수 있다.
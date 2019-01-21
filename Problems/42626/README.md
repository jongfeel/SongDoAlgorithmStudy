# Problem 42626

## 더 맵게

### 문제 설명

매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

> 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- scoville의 길이는 1 이상 1,000,000 이하입니다.
- K는 0 이상 1,000,000,000 이하입니다.
- scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

### 입출력 예

|scoville|s|return|
|--------|-|------|
|[1,2,3,9,10,12]|7|2|

### 입출력 예 설명

1. 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.\
    새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5\
    가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

2. 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.\
    새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13\
    가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3](https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3)

## System Requirement

- Tool: Visual Studio Code
- Extension: Python extension for Visual Studio Code, Python 3.6.5
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "42626" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 배열 길이가 백만이어서 sort 하고 계산하고 하는데 시간 걸리지 않을까 의심하며 코딩 시작
- 역시 하다 보니 런타임 에러 발생, 런타임 에러는 그렇다 치고 그냥 실패한건 이유가 불분명
- 어쨌든 문제 자체가 heap이니까 heap 관련된 자료 구조를 써야 하는게 맞는 거 같아서 sorted heap, priority heap 과 같은 걸로 검색함
- python에 [heapq](https://docs.python.org/3.0/library/heapq.html)라는 좋은 물건이 있어서 이걸로 구현
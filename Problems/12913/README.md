# Problem 12913

## 땅따먹기

### 문제 설명

땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다. 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다. 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

예를 들면,

| 1 | 2 | 3 | 5 |

| 5 | 6 | 7 | 8 |

| 4 | 3 | 2 | 1 |

로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.

마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요. 위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.

### 제한사항

- 행의 개수 N : 100,000 이하의 자연수
- 열의 개수는 4개이고, 땅(land)은 2차원 배열로 주어집니다.
- 점수 : 100 이하의 자연수

### 입출력 예

|land|answer|
|----|------|
|[[1,2,3,5],[5,6,7,8],[4,3,2,1]]|16

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3)

## System Requirement

- Tool: Visual Studio Code
- Extension: Python extension for Visual Studio Code, Python 3.6.5
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "Problem/12913" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 처음부터 column index 0, 1, 2, 3을 하나씩 붙잡고 암산을 해 보면 각 row 별로 큰 수를 결정하는 중요한 조건은 그 이전의 col index의 값을 제외한 나머지 column index 중에 max 값이라는 걸 알 수 있다.
- 이런 식으로 거슬로 올라가면 역시나 Dynamic programming이 된다.
- DP의 큰 특징 중 하나가 내 자신의 값을 결정하기 위해서는 내 이전 값을 확인해야 한다는 조건이므로 DP 문제로 풀어본다.
- 현재 row의 값 중 colomn index 하나를 제외한 max 값은 그 다음 row의 column index의 값으로 결정할 수 있게 구현한다.
  - 즉, 예제에서의 land[1][0]의 값은 5인데 이 5의 값을 결정하는 건 그 이전 row의 column index 0 이 아닌 수 중에 max 값이다.
  - 1, 2, 3, 5 중 column index 0의 값인 1을 제외한 2, 3, 5중의 max는 5이고 이 값은 land[1][0]의 값과 합산 되는 걸 결정한다.
  - 이렇게 해서 land[1][0], land[1][1], land[1][2], land[1][3]을 다 구해보면 최종적으로 아래와 같은 합산된 land로 바뀌게 된다.(land[0] 생략)
  - | 10 | 11 | 12 | 11 |\
    | 4 | 3 | 2 | 1 |
  - 같은 방법으로 land[2][0], land[2][1], land[2][2], land[2][3]을 결정하는 건 그 이전 row의 같은 column index를 제외한 max 값으로 구해볼 수 있다.
  - 그러면 최종적으로 아래와 같은 마지막 array를 구할 수 있다. (land[0], land[1] 생략)
  - | 16 | 15 | 13 | 13 |
  - 마지막 array 중 max 값을 구해보면 16이 나온다는 걸 알 수 있다.
- 결국 column length가 4 이므로 모든 column의 값을 다 체크(brute force)해서 row length 만큼 돌아보면 마지막에는 어떤 column이 최대 값을 가지게 되는지 구할 수 있다.
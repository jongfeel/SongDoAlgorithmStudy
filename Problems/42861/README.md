# Problem 42861

## 섬 연결하기

### 문제 설명

n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

### 제한사항

- 섬의 개수 n은 1 이상 100 이하입니다.
- costs의 길이는 ((n-1) * n) / 2이하입니다.
- 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
- 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
- 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
- 연결할 수 없는 섬은 주어지지 않습니다.

### 입출력 예

|n|costs|return|
|-|-----|------|
|4|[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]|4|

### 입출력 예 설명

costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다.

![https://grepp-programmers.s3.amazonaws.com/files/production/13e2952057/f2746a8c-527c-4451-9a73-42129911fe17.png](https://grepp-programmers.s3.amazonaws.com/files/production/13e2952057/f2746a8c-527c-4451-9a73-42129911fe17.png)

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3](https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3)

## System Requirement

- Tool: Visual Studio Code
- SDK: Python 3.7.2
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "42861" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Understanding graph and algorithm

- 학부 시절 자료구조, 알고리즘을 배웠지만 솔직히 그래프에 대한 건 BFS, DFS, Dijkstra 알고리즘 정도만 기억나고 이번에 한 kruskal 알고리즘은 기억이 하나도 나지 않았다.
- 그래서 다시 공부함
- 알고리즘에 대한 설명과 그림을 보면 이해가 확 된다.
- [https://en.wikipedia.org/wiki/Kruskal%27s_algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)

## Solve - Ready

- 문제 설명에 대한 값을 구하는 것 자체가 최소 신장 트리 알고리즘을 구현하는 것이다. (MST = Minimum Spanning Tree)
- 사실 이걸 알아내려고 끙끙 대는 것 보다 MST 알고리즘을 이해한 후에 구현하는게 훨씬 더 낫다.

## Solve2 - Description

기본적인 작전은 아래와 같다.

- 가장 비용이 적은 순서대로 노드를 다시 나열한다.
- 처음에는 가장 비용이 적은 노드 끼리 나오므로 연결한다.
- 이후 연결되지 않은 노드를 계속 탐색해 나간다.
- 이때 트리 그래프가 깨지지 않는 선에서 탐색하는게 중요하다.
  - 코드에서 findRoot 함수를 통해 연결되어 있는 노드인지를 탐색한다.
- 아직 연결되지 않은 노드가 발견된다면
  - 연결해 주고 그 비용을 더해준다.
  - 비용이 적은 순서대로 탐색해 나가므로 당연한(?) 계산이 된다.
# Problem 42885

## 구명보트

### 문제 설명

무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
- 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

### 입출력 예

|people|limit|return|
|------|-----|------|
|[70, 50, 80, 50]|100|3|
|[70, 50, 50]|100|3|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/42885?language=java](https://programmers.co.kr/learn/courses/30/lessons/42885?language=java)

## System Requirement

- Tool: Visual Studio Code
- SDK: Java SDK 1.8.0_201-b09
- Language: Java

## Test - bash

```bash
javac Problem.java
```

```bash
java Problem
```

## Test - Visaul Studio Code

- Open folder "42885" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve - thinking

- 문제에 답이 있는데 **최대 2명** 밖에 탈 수 없다는 것이다.
- 그렇다는 건 최소한의 구명 보트 수를 구하려면
  - 어떻게든 2명을 태우는 방향으로
  - 그리고 구명보트의 무게제한에 최대한으로 도달하도록 해야 한다.
- 왜냐하면 어차피 40kg이 한명 타나 240kg이 한명 타나 구명보트는 최소 1개가 필요한 거고
- 240Kg의 공간을 효율적으로 채우려면 몸무게가 많이 나가는 사람을 태운 뒤에 남은 공간에 최소 몸무게가 나가는 사람을 태워 나가면 풀린다.

## Solve - programming method

- 왠지 dequeue가 생각 났는데
- 몸무게가 많이 나가는 or 적게 나가는 order로 sort 해 놓고 enqueue, dequeue를 해 나가면 꽤나 깔끔하게 될 거 같았다.
- 생각한 대로 코딩을 해 본다.
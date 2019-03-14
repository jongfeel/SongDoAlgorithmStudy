# Problem 42886

## 저울

### 문제 설명

하나의 양팔 저울을 이용하여 물건의 무게를 측정하려고 합니다. 이 저울의 양팔의 끝에는 물건이나 추를 올려놓는 접시가 달려 있고, 양팔의 길이는 같습니다. 또한, 저울의 한쪽에는 저울추들만 놓을 수 있고, 다른 쪽에는 무게를 측정하려는 물건만 올려놓을 수 있습니다.

![image0.png](https://grepp-programmers.s3.amazonaws.com/files/production/f73e61d4de/f4abf5ff-1956-4e49-bd4a-d3d24619bbf0.png)

저울추가 담긴 배열 weight가 매개변수로 주어질 때, 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값을 return 하도록 solution 함수를 작성해주세요.

예를 들어, 무게가 각각 [3, 1, 6, 2, 7, 30, 1]인 7개의 저울추를 주어졌을 때, 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21입니다.

### 제한사항

- 저울추의 개수는 1개 이상 10,000개 이하입니다.
- 각 추의 무게는 1 이상 1,000,000 이하입니다.

### 입출력 예

|weight|return|
|------|------|
|[3, 1, 6, 2, 7, 30, 1]|21|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/42886?language=python3](https://programmers.co.kr/learn/courses/30/lessons/42886?language=python3)

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

## Solve - Combination

- 저울추 조합(Combination)의 문제로 풀면 되겠지 하고 python을 선택
- 예제의 저울추 7개 정도의 Combination은 얼마 안되니까 통과 되지만 채점하면 죄다 실패함
- 그러면 Combination의 문제가 아닐 수도 있다는 점에 착안 brute force 작전을 씀
- 게다가 문제 전략이 greedy 전략이므로 결정의 순간에 최선의 선택을 하는 쪽을 찾으면 답이 나올 것이라 판단함.

## Solve - Sum

- 예제의 저울추로 하나씩 검증해 본다.
- 일단 나열된 무게추로 측정할 수 없는 최소값을 찾아야 하므로 무게추를 가장 작은 순서대로 다시 나열하고 하나씩 무게추를 추가해서 조합해 보면서 찾아본다.
- [1, 1, 2, 3, 6, 7, 30]
- [1] 최소 1의 무게를 측정할 수 있으므로 통과
- [1, 1] 이 조합으로는 1, 2까지 무게를 측정할 수 있으므로 통과
- [1, 1, 2] 이 조합으로는 1, 2, 3, 4까지 무게 측정 가능... 음?
- [1, 1, 2, 3] 이 조합 역시 1, 2, 3, 4, 5, 6, 7까지 측정 가능?
- 여기까지 해보고 든 생각은 앞에서 부터 차례대로 무게추의 조합으로 측정 가능한 무게의 나열이 다음 무게추에 포함이 되는지 안되는지 여부로 측정 안되는 값을 찾을 수 있을 것 같았다.
- [1, 1, 2, 3, 6] 나열하는게 의미가 없고 1+1+2+3+6이 최대치로 나올 수 있는 조합이므로 13까지 측정 가능하다고 판단할 수 있다. 만약 다음 무게추가 14보다 큰 무게추 라면 측정 불가능한 최소값은 14가 된다는 결론을 얻을 수 있다. 그런데 다음 무게추는 7이라서 7을 더 더한 만큼의 무게추를 측정 가능한 상태로 만들 수 있다. 그러면 20이겠지.
- [1, 1, 2, 3, 6, 7] 이제 나열하는건 의미 없고 1+1+2+3+6+7이 최대치로 나올 수 있는 조합이니까 20까지 측정 가능하다. 그러면 역시 다음 무게추가 21보다 작은 무게추가 등장해야 측정 불가능한 최소값이 21이 아니게 된다.
- [1, 1, 2, 3, 6, 7, 30] 이제 21보다 작은 무게추가 아닌 30이 나왔으므로 측정 불가능한 최소값은 21이다. 덤으로 21 ~ 29까지는 측정할 수 없는 무게가 된다. 왜냐하면 30의 무게추를 포함하는 조합으로 가면 최소 30 + α로 가기 때문이다. 30을 제외한다고 해도 1,1,2,3,6,7을 모두 써봤자 20까지가 측정 가능한 무게이므로 측정 불가능한 최소값이 21이라는 결론을 얻을 수 있다.
- 그리고 사실 무게추의 조합이지만 가장 작은 무게추들의 합 만큼이 최대 무게 측정 가능치라는 걸 알게 된다.
- 약간 내 다음 값이 뭔지를 찾아 나가는 과정이 DP 인 것 같으면서도 index가 아닌 sum 값만 가지고도 간단하게 판단할 수 있는 문제로 보인다.
- 예를 들어 [1, 3]의 무게추가 있다고 하면 최소 측정값은 2라는 걸 바로 파악할 수 있는데, [1]의 무게추에서 다음 측정 가능한 값으로는 2 이하의 무게추가 나와야 하는데 3이 나왔으므로 2가 측정 불가능한 최소값이라는 걸 바로 알아낼 수 있게 된다. 3이 아닌 큰 숫자가 나와도 되며 [1, 5], 3 이후 어떤 무게추가 와도 측정 불가능한 무게 2가 바로 나오기 때문에 의미가 없다. [1, 3, 4, 5, 6, 7, 8, ...]
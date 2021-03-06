# Problem 12971

## 스티커 모으기(2)

### 문제 설명

N개의 스티커가 원형으로 연결되어 있습니다. 다음 그림은 N = 8인 경우의 예시입니다.

![https://res.cloudinary.com/eightcruz/image/upload/v1478590135/%E1%84%89%E1%85%B3%E1%84%90%E1%85%B5%E1%84%8F%E1%85%A5_hb1jty.jpg](https://res.cloudinary.com/eightcruz/image/upload/v1478590135/%E1%84%89%E1%85%B3%E1%84%90%E1%85%B5%E1%84%8F%E1%85%A5_hb1jty.jpg)

원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다. 단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.

예를 들어 위 그림에서 14가 적힌 스티커를 뜯으면 인접해있는 10, 6이 적힌 스티커는 사용할 수 없습니다. 스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return 하는 solution 함수를 완성해 주세요. 원형의 스티커 모양을 위해 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주합니다.

### 제한 사항

- sticker는 원형으로 연결된 스티커의 각 칸에 적힌 숫자가 순서대로 들어있는 배열로, 길이(N)는 1 이상 100,000 이하입니다.
- sticker의 각 원소는 스티커의 각 칸에 적힌 숫자이며, 각 칸에 적힌 숫자는 1 이상 100 이하의 자연수입니다.
- 원형의 스티커 모양을 위해 sticker 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어있다고 간주합니다.

### 입출력 예

|sticker|answer|
|-------|------|
|[14, 6, 5, 11, 3, 9, 2, 10]|36|
|[1, 3, 2, 5, 4]|8|

### 입출력 예 설명

입출력 예 #1\
6, 11, 9, 10이 적힌 스티커를 떼어 냈을 때 36으로 최대가 됩니다.

입출력 예 #2\
3, 5가 적힌 스티커를 떼어 냈을 때 8로 최대가 됩니다.

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12971?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12971?language=python3)

## System Requirement

- Tool: Visual Studio Code
- SDK: Python 3.7.2
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "12971" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve - DP가 아니라고 생각한 방법

- 스티커를 어디서 부터 떼 나가느냐에 따라 다른 거라고 생각해서 경우의 수를 구해보니, 마냥 큰 숫자를 얻기 위해 나머지 숫자를 떼 나가는게 정답이 아니라는 걸 알게 됨
- 그러면 첫번째를 떼느냐 두번째를 떼느냐에 따라 크게 두 가지 경우로 나눠지는데
- 진행해 가면서 내가 어떤 숫자를 선택해서 어떤걸 버리게 될지에 대해 계산해 나가면 답이 구해질 거라 생각했다.
- 느낌엔 DP 였는데 DP로 안하고 할 수 있다고 굳게 믿었는데, 테스트 케이스 정도는 통과하지만 실제 테스트는 통과되지 않는다.

## Solve - DP로 해결

- 결국 테스트가 통과되지 않으므로 DP로 해서 값을 기억해 나가야 한다.
- 첫번째 숫자를 선택하느냐 두번째 숫자를 선택하느냐에 따라 case1, case2가 나뉘며
- 각각 case 별로 초기 점화 숫자를 세팅해 준다.
  - case1
    - sticker[0]을 뗐을 때의 경우다.
    - [0], [1]의 값 모두 sticker[0]으로 준다. DP의 점화식을 위한 세팅이다.
    - sticker[0] + sticker[2]가 크냐, sticker[1]이 크냐 부터 시작할 수 있다.
    - 그 다음부터 i가 증가하면서 경우의 수를 계속 구해 나가고 값을 저장한다.
    - 마지막에 남은 숫자를 구할 때는 첫번째 스티커인 [0]을 똈으므로 [-1]을 버리게 된다.
    - 그러므로 최종적으로 [-2]의 값을 가져와야 최종적으로 남은 숫자를 얻을 수 있다.
  - case2
    - sticker[1]을 뗏을 때의 경우다.
    - [0] = 0, [1] = sticker[1]로 준다.
    - sticker[0] + sticker[2]가 크냐 sticker[1]이 크냐 부터 시작하는데 sticker[0]은 0이니까 결국 sticker[1]이 크냐 sticker[2]가 크냐로 시작한다.
    - 그 다음부터 똑같이 i가 증가하면서 경우의 수를 계속 구해 나간다.
    - 마지막에 남은 숫자를 구할 때는 sticker[0]이 버려졌으므로 sticker[-1]의 값을 가져와야 최종적으로 남은 숫자를 얻을 수 있다.
- 마지막 예외 처리
  - 길이 N이 1 이상이므로 1일 때는 DP 점화식이 구해지지 않는다. 그냥 상식적으로 값이 하나 뿐이므로 sticker[0]의 값을 그냥 return해 준다.
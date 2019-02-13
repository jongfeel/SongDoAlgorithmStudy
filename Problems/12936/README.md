# Problem 12936

## 줄 서는 방법

### 문제 설명

n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다. n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

- [1, 2, 3]
- [1, 3, 2]
- [2, 1, 3]
- [2, 3, 1]
- [3, 1, 2]
- [3, 2, 1]

사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

### 제한사항

- n은 20이하의 자연수 입니다.
- k는 n! 이하의 자연수 입니다.

### 입출력 예

|n|k|result|
|-|-|------|
|3|5|[3,1,2]|

### 입출력 예시 설명

#### 입출력 예 #1

문제의 예시와 같습니다.

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12936?language=python](https://programmers.co.kr/learn/courses/30/lessons/12936?language=python)

## System Requirement

- Tool: Visual Studio Code
- Language: javascript

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "12936" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 문제 보자마자 든 생각은 permutation 문제
- 그리고 풀어야 할 언어는 python.
- 왜냐하면 python에는 permutation을 생성해 주는 라이브러리가 있으니까.
- 그리고 아래와 같은 한 줄로 아름답게 풀 수 있을 것으로 생각했으나 정확성 테스트 12, 13번 통과 안되고 효율성 테스트가 통과가 안됨

```python
list(list(permutations(range(1, n+1)))[k-1])
```

## Solve - advance 1

- 조금 더 생각해 보니 k가 n! 까지 가게 되면 엄청나게 큰 숫자여야 한다. 당장 제한조건인 20!만 해도 매우 큰 숫자이기 때문이다.
- 그래서 쓴 꼼수가 k를 n! / 2로 판단해서 작으면 순서대로 찾고 아니면 index를 거꾸로 찾기 시작하는 걸로 바꾸고
- index를 찾으면 이후는 판단하지 않아도 되므로 바로 return 하는 것으로 바꾸면 해결되지 않을까 싶어서 해봤는데 그냥 잔 기술이었을 뿐이었다.
- 잔기술이라 함은 정확성 테스트 12, 13번 정도는 통과해 주지만 근본적인 문제 해결은 아니라는 뜻이다.

```python
enum = enumerate(permutations(range(1, n+1)))
if (k > math.factorial(n)//2):
    enum = reversed(list(enum))

for index, item in enum:
    if index == k-1:
        return list(item)
```

## Solve - advance 2

- 처음부터 list를 만들 때 k번째인 애를 바로 구하면 되지 않을까? 싶어서 해봄
- 아래 처럼 한줄로 짤 수 있는데, 효율성 테스트는 여전히 실패함

```python
return list(list(item) for index, item in enumerate(permutations(range(1, n+1))) if index == k-1)[0]
```

## Solve - not permutation

- 잔기술인 advance 1 하다가 알게됐는데 2로 나눠서 찾아 나갈꺼면 애초에 k가 permutation의 어느 위치 쯤에 있는지 n으로 나눠가면서 찾을 수 있지 않을까? 싶은 생각이 들었다.
- 즉, 예제에서 보면 permutation 3!의 수 중에 5번째는 [3, 1, 2] 인데 3이 먼저 나열될 수 밖에 없는 순서라는 게 드러난다는 뜻이고 여기서 규칙성을 찾으면 될 거 같았다.
- 그리고 조건에 힌트가 있는데, k는 n! 이하이다. 그러니까 k의 값으로 permutation 순서가 어딘지 구할 수 있다는 뜻이기도 하다.

## Solve - Div, Mod operation

- 예제에서 n!개의 permutation을 굳이 나열할 필요 없이 n의 div, mod 연산으로 해당 index를 찾아 나갈 수 있다.
- 우선 순서가 중요하므로 n! 개의 permutation array의 시작은 [1, 2, 3, ..., n] 으로 하고 여기서 index를 구한 것으로 값을 가져오면 될 것이다.
- Div, mod
  - n! 개에서 처음 수를 구하는 건 n * (n-1)!과 같고 (n-1)의 개수만큼 나눈 몫을 구하면 permutation array 중 첫 index의 값을 구할 수 있다.
  - (n-1)로 나눈 몫은 index로 취하고
  - (n-1)로 나눈 나머지는 다음 (n-2) 범위에서 어디 위치에 있는지 구해야 할지의 숫자 k이므로 이 값도 구해야 한다.
  - index로 쓸 값은 [1, 2, 3]으로 두고 시작한다.
  - 구한 값: []
  - 남은 값: [1, 2, 3]
- 첫번 째 숫자
  - 예제의 n=3, k=5을 보면, (5-1) / (3-1)! = 2로 첫 숫자는 index 2에 해당하는 3의 값이 처음에 온다는 걸 알 수 있다.
  - k번째는 자연수 값이므로 array index 값으로 쓰려면 1을 빼야 한다.
  - 그리고 (5-1) % (3-1)! = 0이 나오고 이 0 값이 이후 (n-2)의 k로 사용할 값이다.
  - 구한 값: [3]
  - 남은 값: [1, 2]
- 두번 째 숫자
  - 그 다음 k는 0, n은 (2-1)!=1, index 값은 0 / 1 = 0이고, 남은 값에서 index 0에 해당하는 값인 1이 그 다음 숫자이다.
  - 위 mod 연산의 나머지 값이 이후 index를 결정할 k이므로 0 % 1 = 0
  - 구한 값: [3, 1]
  - 남은 값: [2]
- 세번 째 숫자
  - 그 다음 k는 0, n은 (1-1)!=1, 그런데 마지막 인덱스이므로 div 연산을 하지 않고 index 그대로 쓴다 그러면 index 0에 해당하는 2의 값이 온다는 걸 알 수 있다.
  - 뭐 굳이 연산을 한다 해도 0 / 1 = 0 이어서 index 0의 2 값을 채워 넣으면 된다.
  - 구한 값: [3, 1, 2]
  - 남은 값: []

## 후기

- 알고리즘의 생각이 올바르면 코드도 그대로 나오게 되는 좋은 예
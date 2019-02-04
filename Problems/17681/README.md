# Problem 17681

## [1차] 비밀 지도

### 문제 설명

비밀지도

네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

1. 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 공백(" ) 또는벽(#") 두 종류로 이루어져 있다.
2. 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 지도 1과 지도 2라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
3. 지도 1과 지도 2는 각각 정수 배열로 암호화되어 있다.
4. 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

![지도1](http://t1.kakaocdn.net/welcome2018/secret8.png)

네오가 프로도의 비상금을 손에 넣을 수 있도록, 비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.

### 제한사항

삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

### 입력 형식

입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.

- 1 ≦ n ≦ 16
- arr1, arr2는 길이 n인 정수 배열로 주어진다.
- 정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 즉, 0 ≦ x ≦ 2<sup>n</sup> - 1을 만족한다.

### 출력 형식

원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.

### 입출력 예제

|매개변수|값|
|-------|--|
|n|5|
|arr1|[9, 20, 28, 18, 11]|
|arr2|[30, 1, 21, 17, 28]|
|출력|["#####","# # #", "### #", "# ##", "#####"]|

|매개변수|값|
|-------|--|
|n|6|
|arr1|[46, 33, 33 ,22, 31, 50]|
|arr2|[27 ,56, 19, 14, 14, 10]|
|출력|["######", "### #", "## ##", " #### ", " #####", "### # "]|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/17681?language=javascript](https://programmers.co.kr/learn/courses/30/lessons/17681?language=javascript)

## System Requirement

- Tool: Visual Studio Code
- Language: javascript

## Test - bash

```bash
node Problem.js
```

## Test - Visaul Studio Code

- Open folder "43105" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 우선 DP 문제라는 개념을 탑재하고 위에서 부터 계산해 내려와 본다.
- 그런데 그렇게 하면 틀린 답으로 가고 있다는 걸 알게 되는데
  - 위에서 부터 내려오면서 중간 분기점에서 숫자가 큰 쪽의 index로 가는게 맞긴 한데
  - 아닌 쪽의 index에서 나중에 훨씬 더 큰 수가 나온다면 낭패! 어찌됐든 틀린답이 된다.
  - 그러면 분기를 탈 때 마다 모든 경우의 수를 구한다 셈 치고 2 x 2 x 2 x 2의 경우의 수인 2<sup>5-1</sup>인 16가지의 경우의 수를 구한 뒤에 여기서 가장 큰 수를 구하면 되는거 아니냐? 할 수 있지만
  - 제한조건의 삼각형의 높이가 500까지이므로 2<sup>500-1</sup>의 경우의 수를 구하는 게 아니라는 걸 빨리 깨달아야 한다.
- 그러면 밑에서 부터 거꾸로 올라가면서 푸는 DP 문제라는 걸 깨닫게 됨
- 푸는 방법
  - 가장 하단의 숫자 들 중 인접한 두 수 중에 큰 숫자를 가져온다.
  - 왜냐하면 바로 위에서 내려오면서 큰 숫자를 구한다면? 의 역 가정이니까
  - 예제에서 마지막 줄의 4, 5, 2, 6, 5의 경우 바로 위 index에서 각 선택지가 (4, 5), (5, 2), (2, 6), (6, 5)로 갈리게 된다.
  - 그러므로 이 숫자들 중 큰 숫자를 구하면 5, 5, 6, 6이 되고
  - 이걸 위 index의 2, 7, 4, 4와 합하면 7, 12, 10, 10이 된다.
  - 7, 12, 10, 10 역시 인접한 두 수 중 큰 숫자를 구해서 바로 위 index와 합해준다.
  - 이런 식으로 계산해 올라가면 최종 array[0]의 값은 가장 큰 수인 30을 얻을 수 있다.
- DP 문제의 당연한 논리 이므로 잘 이해가 안되면 DP를 먼저 이해하면 된다.
  - DP의 기본 논리는 지금 내 index의 값을 구하기 위해서 내 이전 index인 index-1이나 index-2까지 값을 구해 나가는 문제이다.
  - 역으로 index+2를 구하고 싶으면 index+1을 구하고 index+1 역시 index를 구하면 값을 자연스럽게 얻을 수 있는 문제가 DP 문제

## Javascript

- 예제의 array 마지막 index 5개의 element를 4개로 줄이는 작업을 하는 거라, 바로 javascript의 reduce를 떠올렸다.
- 다음 accumulator 수를 current의 값으로 계속 return 하고
- Math.max(accumulator, current)를 따로 array로 담으면 되겠거니 하고 이미 머리속에 javascript로 풀 생각을 한 뒤에 바로 풀어봄
- 그런데 풀어보고 난 후에 이 문제에 효율성 테스트는 통과 못하겠구나를 직감했는데, 왜냐하면 reduce 함수에서 accumulator는 이전 callback의 return 값으로 오는 구조여서 recursive fuction stack 때문에 반드시 시간 초과가 나겠구나 싶었다.
- 역시나 해보니 모든 효율성 테스트 실패!
- 그냥 jagged array 구조니까 for문 두번 돌리는게 효율성 통과하는 방법.

## One more thing, python

- 사실 javascript의 성능은 크게 기대할 바는 아닌 건 맞는데, 혹시 C++이나 python으로 하면 어떨까? 싶어 궁금해서 해봄 (Java는... 음...)
- 왜냐하면 삼각형 높이 max인 500 까지 recursive fuction stack이 쌓이면 효율성이 낮은건 맞지만
  - 고작 하는 계산이라고는 max값 구하고 array에 추가하는 거 뿐인데다
  - 10,000 or 100,000 stack의 수준도 아니고 고작 500 stack 수준에서 통과가 안되는게 궁금했다.
- 일단 python으로 먼저 해봤는데 javascript와 다르게 python에서 구현한 특징은
  - javascript와 같이 reduceRight 같은 함수를 지원하지 않으므로 처음부터 list(reverse(triangle))로 뒤집고 시작한다. (설마 reduceRight 성능이 낮은 건 아닐까? 하고 해봤지만 결과는 같음)
  - accumulator에 해당하는 부분을 익명인 lambda로 구현할 수 없는데, lambda는 multiline으로 구현할 수 없으므로 함수를 따로 def 해서 구현
  - 아랫줄의 서로 인접한 수 중 큰 수의 array와 자신의 array 에서 같은 index끼리 더하는 과정에서 javascript 처럼 map을 쓰는게 아니라 python의 특징인 zip으로 묶어서 for문을 돌리면 효율적으로 구현 가능
- 효율성 테스트에서 대략 27 ~ 34ms의 시간이 소요되는데 효율성 테스트가 통과됨
- 효율성 테스트 통과하는 모습을 보고 다시 한번 python의 놀라운 능력에 감탄
- CLI에서 바로 import this를 입력하고 zen of python 리뷰를 해본다.
  - If the implementation is easy to explain, it may be a good idea.

``` python
import this
```
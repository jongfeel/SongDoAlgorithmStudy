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

- Open folder "17681" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- python은 훌륭한 언어이나, 이건 특별히 javascript로 짜보고 싶었다.
- 이유는
  - javascript에 bitwise 문법이 얼마나 아름다운 코드로 나올지 머릿속에 그려지는 걸 구현해 보고자 함
  - "#"으로 출력하는 건 array, map으로 이어지는 구현이 떠올랐는데 가장 먼저 떠오른 javascript가 그나마 익숙(?)한 언어여서 그럴 걸지도
- 두 array인 arr1과 arr2의 각 item index들 끼리 or 연산을 해 준다.
- 10진수를 or 연산 해도 내부적으로는 2진수 bitwise or 연산이 된다. => 의심되면 직접 2진수에 해당하는 10진수 가지고 or (|) 연산을 해 보면 된다.
- or 연산을 한 뒤 합쳐진 arr을 map을 거쳐서 1이면 "#", 0이면 " "로 해서 string 출력을 해 주면 결과를 얻을 수 있다. javascript 문법을 십분 활용해서 진행해 본다.
  - toString(2): 2진수 변환
  - split(""): string을 char array로 변환
  - map(): 위에서 설명
  - join(""): array의 각 index 값을 합쳐준다

## One more thing

- 예제에 이미 함정이 있는데 두번 째 예제를 돌려보면 n의 길이 만큼 arr의 2진수의 길이가 맞춰져야 한다는 점을 찾을 수 있다.
- 예제 2번의 경우 2진수로 변환하면 n이 6이므로 다 6자리로 맞춰질 거 같은데 사실 앞에 0이 있는 2진수의 경우는 무시가 된다. 예로 index 4 의 OR 연산을 한 결과 값으로 오는 31의 경우는 11111로 채워지는 정직한 2진수의 값인데 n은 6으로 되어 있으므로 사실 011111로 채워져야 하고 이걸 string으로 표현해서 " #####"으로 나오게 해야 한다.
- 그래서 map 까지 된 결과를 가지고 그 length가 n까지 도달하지 못한 mappingResult의 경우는 uhshift(" ") 함수를 걸어준다.
- unshift는 arr의 index 0 부터 값을 채워넣는 함수이므로 2진수 앞의 0에 해당하는 " " 공백을 채워넣기에 효과적인 함수이다.

## More effective javascript

- 이왕 javascript 짠 거 더 기교를 부려본다.
- Array.keys()는 iterator를 return 해 주므로 rest operator (...)와 결합하면 array가 생성된다. 마치 python range나 c#의 Enumerable.Range, java의 IntStream.range와 같은 느낌으로 쓸 수 있다.
- 한가지 구멍은 python, c#, java와 달리 start 값을 지정해 줄 수 없다는 것이다. 조만간 ecmascript에서 range를 만들어야 하지 않을까 싶다.
- 물론 loadash, underscore에 있는 걸 쓰면 되지 않냐? 라고 생각할 수 있지만 다른 언어에서는 언어 스펙에서 제공하는 거라 좀 다른 얘기다.

``` javascript
[...Array(3).keys()]
// [0, 1, 2]
```

- 개인적으로 for 계열 (for, foreach, while, do while 등등)과 if 계열 (if, switch 등)을 쓰지 않고 코드를 짜는 걸 즐기면 코드양이 대폭 줄어들고 뿌듯함을 느낄 수 있다.
- 여기서의 뿌듯함은 문법적으로 많이 알고 즐기는 것 뿐인 것이지 효율적이거나 가독성이 항상 좋다는 걸 의미하지는 않는다.
- 그리고 최대 단점으로는 익숙하지 않으면 한번에 쉽게 알아보기 힘들다는 것 정도.
- Readability vs Simplicity 의 갈등인데 이런 기교는 본인이 필요할 때 하는게 좋은 것 같고, 처음에 짠 코드가 더 가독성이 있어 보일 수 있다.
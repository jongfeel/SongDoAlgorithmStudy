# Problem 17677

## 뉴스 클러스터링

### 문제 설명

여러 언론사에서 쏟아지는 뉴스, 특히 속보성 뉴스를 보면 비슷비슷한 제목의 기사가 많아 정작 필요한 기사를 찾기가 어렵다. Daum 뉴스의 개발 업무를 맡게 된 신입사원 튜브는 사용자들이 편리하게 다양한 뉴스를 찾아볼 수 있도록 문제점을 개선하는 업무를 맡게 되었다.

개발의 방향을 잡기 위해 튜브는 우선 최근 화제가 되고 있는 카카오 신입 개발자 공채 관련 기사를 검색해보았다.

- 카카오 첫 공채..'블라인드' 방식 채용
- 카카오, 합병 후 첫 공채.. 블라인드 전형으로 개발자 채용
- 카카오, 블라인드 전형으로 신입 개발자 공채
- 카카오 공채, 신입 개발자 코딩 능력만 본다
- 카카오, 신입 공채.. 코딩 실력만 본다
- 카카오 코딩 능력만으로 2018 신입 개발자 뽑는다

기사의 제목을 기준으로 블라인드 전형에 주목하는 기사와 코딩 테스트에 주목하는 기사로 나뉘는 걸 발견했다. 튜브는 이들을 각각 묶어서 보여주면 카카오 공채 관련 기사를 찾아보는 사용자에게 유용할 듯싶었다.

유사한 기사를 묶는 기준을 정하기 위해서 논문과 자료를 조사하던 튜브는 자카드 유사도라는 방법을 찾아냈다.

자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다. 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.

예를 들어 집합 A = {1, 2, 3}, 집합 B = {2, 3, 4}라고 할 때, 교집합 A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}이 되므로, 집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다. 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.

자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다. 다중집합 A는 원소 1을 3개 가지고 있고, 다중집합 B는 원소 1을 5개 가지고 있다고 하자. 이 다중집합의 교집합 A ∩ B는 원소 1을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 1을 max(3, 5)인 5개 가지게 된다. 다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면, 교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}가 되므로, 자카드 유사도 J(A, B) = 3/7, 약 0.42가 된다.

이를 이용하여 문자열 사이의 유사도를 계산하는데 이용할 수 있다. 문자열 FRANCE와 FRENCH가 주어졌을 때, 이를 두 글자씩 끊어서 다중집합을 만들 수 있다. 각각 {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}가 되며, 교집합은 {FR, NC}, 합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}가 되므로, 두 문자열 사이의 자카드 유사도 J("FRANCE", "FRENCH") = 2/8 = 0.25가 된다.

### 입력 형식

- 입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.
- 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 예를 들어 ab+가 입력으로 들어오면, ab만 다중집합의 원소로 삼고, b+는 버린다.
- 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. AB와 Ab, ab는 같은 원소로 취급한다.

### 출력 형식

입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로, 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

### 예제 입출력

|str1|str2|answer|
|----|----|------|
|FRANCE|french|16384|
|handshake|shake hands|65536|
|aa1+aa2|AAAA12|43690|
|E=M*C^2|e=m*c^2|65536|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3](https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3)

## System Requirement

- Tool: Visual Studio Code
- SDK: Python 3.7.2
- Language: Python

## Test - bash

```bash
python Problem.py
```

## Test - Visaul Studio Code

- Open folder "17677" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve - 착각

- 집합(set) 문제여서 python에 set을 이용하면 바로 intersection과 union함수를 호출해서 결과를 얻을 수 있다는 걸 알아냄
- 심지어 함수 호출 말고 연산자를 통해서도 구할 수 있는데
  - Union 구하기: setA | setB
  - Intersection 구하기: setA & setB
  - 이렇게 쉽게 구할 수 있다.
- 그런데 문제를 끝까지 안읽고 함정에 빠지고 말았으니, 문제에는 다중집합으로 구하는 방법에 대해 얘기해 주고 있었는데 정작 set은 중복값을 허용하지 않아서 문제를 풀 수가 없었다.

## Solve - 원래 집합의 개념대로 구현

- 그래서 set을 다시 list로 바꿔서 진행했다.
- 글자 두개씩 집합으로 만드는 건 for문을 돌려서 현재 index i와 다음 index i+1을 합치면 된다. 이렇게 하려면 len - 1만큼만 돌아야 한다.

```python
for i in range(0, len(str1) - 1):
        twochar = str1[i] + str1[i+1]
```

- 영문자를 판별하는 건 isalpha() 함수를 호출해 준다.

``` python
if twochar.isalpha() == True:
```

- 그리고 list에 넣어줄 때는 lower() 함수를 호출해서 대소문자 구분 없이 다 소문자로 넣는다.

``` python
setA.append(twochar.lower())
```

- setB도 마찬가지로 해서 두 set을 준비한다.
- 그리고 각각 복사본을 준비해서 union, intersection을 구할 준비를 한다.
- union
  - union은 setA와 setB에 하나라도 있으면 포함시킨다.
  - for문은 setA 기준으로 돌아가므로 setB에 setA의 원소가 있는지 확인한다.
  - 있으면 setB에 있는 같은 원소는 있을 필요가 없으므로 지운다.
  - 이런식으로 돌면 setA 기준으로 setB에 있는 원소는 모두 제거된다.
  - 그리고 setA와 남은 setB의 원소를 모두 합하면 union을 구할 수 있다.

  ``` python
  union = []
    for a in setA_copy:
        if a in setB_copy:
            #print(a)
            setB_copy.remove(a)
    union = setA_copy + setB_copy
  ```

- intersection
  - intersection은 setA와 setB에 원소가 같이 있는지 판단한다.
  - setA 기준으로 for문을 돌고 setB에 같은 원소가 있다면 intersection list에 추가해 준다.
  - 한가지 주의해야 할 건 setA, setB에 동시에 있는 원소였으므로 setB에 해당 원소를 삭제해야 하는데, 이게 다중집합이 아닐 경우에는 안해도 되는데 같은 값을 가지는 원소가 있을 수 있으므로 지워야 한다.

  ``` python
  intersection = []
    for a in setA_copy:
        if a in setB_copy:
            #print(a)
            intersection.append(a)
            setB_copy.remove(a)
  ```

- Jaccard similarity
  - 이제 자카드 유사도를 구해야 하는데
  - 어떤 언어든지 나눗셈을 해봤다면 0으로 나누면 안된다는 사실을 잊으면 안된다.
  - 그래서 union count가 0일 때는 65536을 return해주는 코드를 추가해 준다.

  ``` python
  if unionCount == 0:
        return 65536
    return (int)(intersectionCount / unionCount * 65536)
  ```
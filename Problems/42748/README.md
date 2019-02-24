# Problem 42748

## K번째수

### 문제 설명

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- array의 길이는 1 이상 100 이하입니다.
- array의 각 원소는 1 이상 100 이하입니다.
- commands의 길이는 1 이상 50 이하입니다.
- commands의 각 원소는 길이가 3입니다.

### 입출력 예

|array|command|return|
|-----|-------|------|
|[1, 5, 2, 6, 3, 7, 4]|[[2, 5, 3], [4, 4, 1], [1, 7, 3]]|[5, 6, 3]|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/42748?language=go](https://programmers.co.kr/learn/courses/30/lessons/42748?language=go)

## System Requirement

- Tool: Visual Studio Code
- SDK: go1.11.5 windows/amd64
- Language: go

## Test - bash

```bash
go build Problem.go
```

```bash
Problem.exe
```

## Test - Visaul Studio Code

- Open folder "42748" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 문제가 쉬운 편이라 특별히 설명을 하는게 이상할 정도
- Go 언어로 하다 보니 특이점이 있는데
  - sub array를 가져오려면 origin array의 복사본을 가져와서 해야 한다.
  - make 함수가 copy를 해 주는 함수이다.
  - sub array 가져오는 방법은 의외로 tmp[start:end]범위를 지정해 주면 가져와진다.
- array 추가하는 함수는 append 인데 값을 담을 array를 파라미터로 주고, 그 결과를 return으로 받아야 한다.
# Problem 12919

## 서울에서 김서방 찾기

### 문제 설명

String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요. seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

### 제한 사항

- seoul은 길이 1 이상, 1000 이하인 배열입니다.
- seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
- Kim은 반드시 seoul 안에 포함되어 있습니다.

### 입출력 예

|seoul|return|
|-|------|
|["Jane", "Kim"]|"김서방은 1에 있다"|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12919?language=csharp](https://programmers.co.kr/learn/courses/30/lessons/12919?language=csharp)

## System Requirement

- Tool: Visual Studio Code
- SDK: .NET Core 2.1.403
- Language: C#

## Test - bash

```bash
dotnet build
```

```bash
dotnet run
```

## Test - Visaul Studio Code

- Open folder "12919" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- Array의 index를 찾으면 되는 문제
- C#의 FindIndex method를 사용해서 "Kim"의 index를 찾는다.
  - Linq를 사용해 predecate를 lambda로 구현한다.
- C#의 string inerpolation으로 간결하게 string formatting을 한다.
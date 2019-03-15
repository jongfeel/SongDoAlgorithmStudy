# Problem 42747

## H-Index

### 문제 설명

H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

### 입출력 예

|citations|return|
|---------|------|
|[3, 0, 6, 1, 5]|3|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/42747?language=csharp](https://programmers.co.kr/learn/courses/30/lessons/424747language=csharp)

## System Requirement

- Tool: Visual Studio Code
- SDK: .NET Core 2.1.600-preview-009497
- Language: C#

## Test - bash

```bash
dotnet build
```

```bash
dotnet run
```

## Test - Visaul Studio Code

- Open folder "42747" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 얼마나 인용됐는지 확인하기 위해 문제 조건대로 0 to 10000 만큼 loop를 돌린다.
- 인용 횟수만큼 논문 편수가 있는지 where 조건으로 확인하고 이하인 조건이 발견되면 그 인용 횟수를 리턴한다.
- 문제에 답이 있는데, 착각한게 뭐냐면
  - 인용된 횟수니까 == 기준으로 판단하면 된다고 생각했는데, 이렇게 하면 테스트 케이스 11번을 통과하지 못한다.
  - 이유를 생각해 보면 이하 조건으로 하지 않을 경우 영원히 인용 횟수 만큼의 논문 갯수를 찾지 못하는 경우가 있다.
- 논문 n편이 h번 이상 인용과 나머지 그러니까 length - n편이 h번 이하에서 length가 홀수일 경우 인용 횟수가 일치하지 않는 교차 지점이 있다.
  - 전체 논문 7편 중 4편이 3번 이상 인용, 나머지 3편이 4번 이상 인용의 가능성이 존재할 수 있음
  - 아래 코딩도장 설명 글 참조
  - [http://codingdojang.com/scode/491](http://codingdojang.com/scode/491)
- 그래서 이상, 이하 조건대로 코드를 짜야 한다는게 결론. 그러면 테스트 케이스 11번도 통과됨
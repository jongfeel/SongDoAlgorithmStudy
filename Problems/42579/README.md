# Problem 42579

## 베스트앨범

### 문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

### 제한 사항

- genres[i]는 고유번호가 i인 노래의 장르입니다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
- 장르 종류는 100개 미만입니다.
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
- 모든 장르는 재생된 횟수가 다릅니다.

### 입출력 예

|genres|plays|return|
|------|-----|------|
|["classic", "pop", "classic", "classic", "pop"]|[500, 600, 150, 800, 2500]|[4, 1, 3, 0]|

### 입출력 예 설명

classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

- 고유 번호 3: 800회 재생
- 고유 번호 0: 500회 재생
- 고유 번호 2: 150회 재생

pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

- 고유 번호 4: 2,500회 재생
- 고유 번호 1: 600회 재생

따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/42579?language=csharp](https://programmers.co.kr/learn/courses/30/lessons/42579?language=csharp)

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

- Open folder "42579" by Visual Studio Code
- Check out settings - launch.json
- Press F5 to debug start

## Solve

- 문제를 보며 든 생각은 아래 두가지였다.
  - DB를 할 줄 아는 사람이면 문제 풀어나가는 방법을 쉽게 알 수 있겠구나
  - 오랜만에 C# Linq의 GroupBy를 써보면 아름다운 코드가 나오겠구나
- 처음에 할 일은 각각 array로 나눠진 고유번호별 genres와 plays를 묶어서 DB Table 처럼 관리해야 한다.
  - bestDic은 고유번호별 genre와 play를 묶어서 저장한 dictionary이다.

``` csharp
Dictionary<int, KeyValuePair<string, int>> bestDic = new Dictionary<int, KeyValuePair<string, int>>();
for (int i=0; i<genres.Length; i++)
{
    bestDic.Add(i, new KeyValuePair<string, int>(genres[i], plays[i]));
}
```

- 우선 genres 별로 최대 plays를 구해야 한다.
  - DB query를 해봤다면 group by와 order by가 저절로 떠오를 것이고 select 절에 sum 함수를 쓰면 된다는게 머리속에 떠올랐을 것이다.
  - 그걸 C#의 Linq로 구하면 아래와 같이 된다.
  - genre와 play로 묶인 Values를 genre로 GroupBy 해 준 후에 다시 ToDictionary를 통해 key, value로 만들어 주는데 이 때 value를 genre별 play의 sum값으로 해 준다.
  - 그리고 OrderByDescending을 통해 최대 play수 별 genre를 나열할 수 있게 된다.

``` csharp
// [ {"pop", 3100}, {"classic", 1450} ]
var groupByGenresDic = bestDic.Values.GroupBy(g => g.Key).ToDictionary(k => k.Key, v => v.Sum(vv => vv.Value)).OrderByDescending(o => o.Value);
```

- 그 후 genre별 최대 play수 대로 고유번호를 최대 2개를 가져오면 되는데, 각 genre별 최대 play 순서 대로 가져오는 건 아래와 같이 하면 된다.
  - Where 메소드를 통해 genre별 최대 play수대로 정리된 groupByGenresDic을 돌면서 bestDic에서 맞는 genre를 찾아내서 play수가 높은 순서대로 나열하고 최대 2개를 가져오는 코드를 짠다.
  - C#의 Take(2) 메소드의 고마운 점은 최대 2개 까지 가져온다는 생각대로 동작한다는 것이다. 즉, 1개만 있다면 1개만 가져오고 맞는 것이 없다면 가져오지 않는다.
  - 가져온 generesIndexDic의 Key를 보면 조건에 맞는 고유번호들이 들어있다는 걸 확인할 수 있다.
  - 이걸 answer list에 차례로 추가해 둔다.

``` csharp
foreach (var item in groupByGenresDic)
{
    // [{4, {"pop", 2500}}, {1, {"pop", 600}}, ...]
    var generesIndexDic = bestDic.Where(w => w.Value.Key == item.Key).OrderByDescending(o => o.Value.Value).Take(2);
    foreach (var item2 in generesIndexDic)
    {
        // Console.WriteLine(item2.Key);
        answer.Add(item2.Key);
    }
}
```

- 마지막으로 고유번호가 담긴 answer를 ToArray() 메소드 호출을 통해 return 해 준다.

``` csharp
return answer.ToArray();
```

# Problem 12901

## 2016년

### 문제 설명

2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각
SUN,MON,TUE,WED,THU,FRI,SAT

입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.

### 제한 조건

- 2016년은 윤년입니다.
- 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

### 입출력 예

|a|b|result|
|-|-|------|
|5|24|TUE|

### 문제 링크

[https://programmers.co.kr/learn/courses/30/lessons/12901?language=ruby](https://programmers.co.kr/learn/courses/30/lessons/12901?language=ruby)

## System Requirement

- Tool: None, cmd
- Installer: Ruby+Devkit 2.5.3-1 (x64)
- Language: Ruby 2.5.3p105
- Download: [https://rubyinstaller.org/downloads/](https://rubyinstaller.org/downloads/)

## Test - bash

```bash
ruby Problem.rb
```

## Solve

- 모든 프로그래밍 언어에는 date time 관련된 함수를 제공한다.
- ruby에 있는 Time 객체를 생성할 때 2016년과 parameter로 넘어온 a와 b를 월, 일로 넣어준다.
- strftime은 time formatting 함수로 이 역시 어느 언어에나 있는 함수로 %a를 출력하면 해당 날짜의 week of day를 소문자로 출력한다.
  - 참고로 %A로 하면 fullname day of week가 출력된다. Monday, Tuesday...
- upcase를 추가로 호출해 문제 조건에 맞게 대문자로 출력해 준다.

## More solves

- ruby가 한줄로 끝나서 심심하니 다른 언어들은 어떤지 살펴본다.

### C++

- 그런거 없다. time_t 구조체를 써야 하고, mktime, localtime 함수를 거쳐서 최종적으로 dayofweek에 해당하는 int 값을 구할 수 있다. 그리고 그걸 string으로 바꿔주면 된다.
- 놀랍게도 day of week를 string으로 바꿔주는 코드를 제외하고도 나온 코드량이 이정도여서 C++로는 day of week 구하는게 쉽지 않음을 알 수 있다.

``` cplusplus
std::tm time_in = { 0, 0, 0, // second, minute, hour
      24, 4, 2016 - 1900 }; // 1-based day, 0-based month, year since 1900

  std::time_t time_temp = std::mktime(&time_in);

  //Note: Return value of localtime is not threadsafe, because it might be
  // (and will be) reused in subsequent calls to std::localtime!
  const std::tm * time_out = std::localtime(&time_temp);

  //Sunday == 0, Monday == 1, and so on ...
  cout << "Today is this day of the week: " << time_out->tm_wday << "\n";
```

### C#

- C#은 .NetFramework의 강력한 DateTime library가 있기 때문에 역시 한줄로 끝낼 수 있다.
- Formating에 "ddd"는 day of week를 3글자로 표현하는 것이고 ToUpper() 메소드를 통해 대문자로 표현한다.

``` csharp
new DateTime(2016, 5, 24).ToString("ddd").ToUpper()
```

### Java

- Java 역시 DayOfWeek enum과 LocalDate class를 가지고 만들어 낼 수 있다. C#과 달리 조금 java 스러운 method chaining을 거치긴 해야 하지만 어쨌든 한 줄로 결과를 얻을 수 있긴 하다.
- getDisplayName을 통해 day of week를 어떻게 출력할 지 결정하고 이후 toUpperCase() 메소드를 통해 대문자로 표현한다.

``` Java
DayOfWeek.from(LocalDate.of(2016, 5, 24)).getDisplayName(TextStyle.SHORT, Locale.US).toUpperCase()
```

### Javascript

- Javascript 역시 Date class를 지원하고 여기서 toLocaleString으로 옵션을 주면 day of week를 얻을 수 있다.
- 주의할 점: javascript에서 month는 c 계열을 따르는지 1월이 0부터 시작한다.
- 마찬가지로 toUpperCase()를 호출해서 대문자로 바꿔야 한다.

``` javascript
new Date(2016, 4, 24).toLocaleString('en-us', {  weekday: 'short' }).toUpperCase()
```

### Python

- python 역시 datetime을 지원하기 때문에 쉽게 얻을 수 있다. 재미있는건 format method와 formatter string이 ruby와 같다는 점이다.

``` python
datetime.datetime(2016,5,24).strftime("%a").upper()
```

### Swift

- swift는 한 줄로 얻을 수 없다.
- formatter를 거쳐야 하고, Date를 특정 년월일로 생성하는게 불가능하다.
- 그리고 Calendar를 사용해서 dayofweek를 얻어내야 하기 때문에 코드양이 생각보다 많아진다. 다른 언어에 비해 뜻밖의 패배를 했다고 볼 수 있다.
- 놀라운건 아래 코드는 현재 날짜인 Date()를 통해 구하는 코드이므로 특정 년월일로 해주는 코드를 짜려면 코드를 더 추가해야 한다.

``` Swift
let customDateFormatter = DateFormatter()

print(customDateFormatter.weekdaySymbols[Calendar.current.component(.weekday, from: Date())])
```

## Results

- programmers 문제에서 제한된 언어만을 봤을 때 제일 직관적이고 짧은 코드는 javascript 정도인 것 같다.
- java는 직관적인데 코드가 좀 길고, ruby와 python은 %a가 C#은 ddd가 직관성을 조금 떨어뜨린다.
- C++과 swift로 day of week를 구하는 건 꽤나 귀찮은 일이라는 점 까지가 결론
from itertools import combinations

def solution(weight):
    #print(sorted(weight)[0:7])
    #for item in list(combinations(sorted(weight)[0:7], 6)):
        #print(sum(item))
    answer = 1 # 무게추 들의 합까지를 측정할 수 있고 그다음 무게가 측정할 수 없는 값이므로 1부터 시작
    for w in sorted(weight):
        if answer < w:
            break
        answer += w
    return answer

print(solution([3, 1, 6, 2, 7, 30, 1]))
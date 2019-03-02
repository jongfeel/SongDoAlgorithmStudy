from itertools import combinations

def solution(weight):
    #print(sorted(weight)[0:7])
    #for item in list(combinations(sorted(weight)[0:7], 6)):
        #print(sum(item))
    answer = 1
    for w in sorted(weight):
        if answer < w:
            break
        answer += w
    return answer

print(solution([3, 1, 6, 2, 7, 30, 1]))
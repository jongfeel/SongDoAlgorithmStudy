def solution(scoville, K):
    answer = -1
    scoville = sorted(scoville)
    for i in range(1, len(scoville)):
        scoville[i] = scoville[i-1] + scoville[i] * 2
        if scoville[i] >= K:
            return i
        del scoville[i]
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
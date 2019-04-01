def hanoi(n, from_pos, to_pos, aux_pos, answer):
    if n == 1:
        answer.append([from_pos, to_pos])
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos, answer)
    answer.append([from_pos, to_pos])
    hanoi(n - 1, aux_pos, to_pos, from_pos, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    #print(answer)
    return answer

print(solution(2))

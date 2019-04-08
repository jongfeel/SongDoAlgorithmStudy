def solution(n, money):
    answer = 0
    changes = [0] * 100001
    changes[0] = 1
    for m in money:
        for count in range(1, n+1):
            if count - m >= 0:
                changes[count] += changes[count - m] % 1000000007
    
    #for k in range(0, n+1):
        #print(changes[k])
    
    answer = changes[n]
    return answer

print(solution(5, [1,2,5]))

#from itertools import permutations
import math

def solution(n, k):
    
    # try1: 정확성 테스트 12, 13 빼고 통과, 효율성 모두 실패
    #return list(list(permutations(range(1, n+1)))[k-1])
    
    # try 2: 정확성 모두 통과, 효율성 모두 실패
    #print(list(list(item) for index, item in enumerate(permutations(range(1, n+1))) if index == k-1)[0])
    #return list(list(item) for index, item in enumerate(permutations(range(1, n+1))) if index == k-1)[0
    
    # try3: 모두 성공
    nextK = k-1
    startArray = list(range(1, n+1))
    answer = []
    
    while n-1:
        n -= 1
        index = nextK // math.factorial(n)
        nextK = nextK % math.factorial(n)
        #print(f"index: {index}")
        #print(f"nextK: {nextK}")
        answer.append(startArray[index])
        del startArray[index]
            
    answer.append(startArray[0])
    return answer

print(solution(3, 5))
print(solution(5, 70))
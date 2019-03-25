from functools import reduce

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    # 1. for loop accumulate answer
    '''
    answer = arr[0]
    for index in range(len(arr)-1):
        answer = lcm(answer, arr[index+1])
    return answer
    '''
    
    #2. using reduce func
    return reduce(lcm, arr)
    
    #3. using reduce and implement func for lcm by lambda
    #return reduce(lambda a, b: a * b // gcd(a, b), arr)

#168
print(solution([2, 6, 8, 14]))

#6
print(solution([1, 2, 3]))

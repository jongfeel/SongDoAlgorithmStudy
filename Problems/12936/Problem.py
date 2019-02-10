
def solution(n, k):
    ''' solve - advance
    enum = enumerate(permutations(range(1, n+1)))
    if (k > math.factorial(n)//2):
        enum = reversed(list(enum))
        
    for index, item in enum:
        if index == k-1:
            return list(item)
    '''

    # first solve
    # return list(list(permutations(range(1, n+1)))[k-1])

    # second solve
    # return list(list(item) for index, item in enumerate(permutations(range(1, n+1))) if index == k-1)[0]

    return 0

print(solution(3, 5))
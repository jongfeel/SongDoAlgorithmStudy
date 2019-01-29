from functools import reduce

maxArr = []

def reduceCol(acc, cur):
    maxArr.append(max(acc, cur))
    return cur

def reduceRow(acc, cur):
    #print(acc),
    #print(cur),
    reduce(reduceCol, acc)
    #print(maxArr)
    newAcc = [x + y for x, y in zip(maxArr, cur)]
    #print(newAcc)
    del maxArr[:]
    return newAcc

def solution(triangle):
    triangle = list(reversed(triangle))
    return reduce(reduceRow, triangle)[0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
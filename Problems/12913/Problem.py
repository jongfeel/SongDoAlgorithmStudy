def solution(land):
    loopLen = len(land)-1
    
    for idx, row in enumerate(land):
        if idx == loopLen:
            break
        land[idx+1][0] += max(row[1], row[2], row[3])
        land[idx+1][1] += max(row[0], row[2], row[3])
        land[idx+1][2] += max(row[0], row[1], row[3])
        land[idx+1][3] += max(row[0], row[1], row[2])

    return max(land[len(land)-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
def solution(sticker):
    stickerLength = len(sticker)
    
    if stickerLength == 1: return sticker[0]
    
    case1 = [0] * stickerLength
    case2 = [0] * stickerLength
    
    case1[0] = sticker[0]
    case1[1] = sticker[0]
    
    #case2[0] = 0
    case2[1] = sticker[1]
        
    for i in range(2, stickerLength):
        case1[i] = max(case1[i-1], case1[i-2] + sticker[i])
        case2[i] = max(case2[i-1], case2[i-2] + sticker[i])
    
    return max(case1[stickerLength - 2], case2[stickerLength - 1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
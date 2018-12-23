import Foundation

func solution(_ board:[[Int]]) -> Int
{
    var answer:Int = 0
    
    var copyboard = [[Int]](repeating: [Int](repeating: 0, count: board[0].count), count: board.count)
    
    for x in 0 ..< board.count {
        for y in 0 ..< board[x].count {
            copyboard[x][y] = board[x][y]
        }
    }
    
    if copyboard.count == 1 || copyboard[0].count == 1 {
        for x in 0 ..< board.count {
            for y in 0 ..< board[x].count {
                if copyboard[x][y] == 1 {
                    answer = 1
                    break
                }
            }
        }
    }
    
    var minVal:Int = 0
    for x in 0 ..< copyboard.count-1 {
        for y in 0 ..< copyboard[x].count-1 {
            minVal = min(copyboard[x][y], copyboard[x][y+1], copyboard[x+1][y])
            if copyboard[x+1][y+1] != 0 {
                copyboard[x+1][y+1] = minVal + 1
                answer = max(answer, copyboard[x+1][y+1])
            }
        }
    } 
    
    /*for x in 0 ..< board.count {
        for y in 0 ..< board[x].count {
            print(copyboard[x][y])
        }
    }*/

    return answer * answer
}

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
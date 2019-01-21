import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    var ans = 0
    
    var copyA = A
    copyA.sort()    // <
    var copyB = B
    copyB.sort(by: >)
    //print(copyA)
    //print(copyB)
    
    for (itemA, itemB) in zip(copyA, copyB) {
        ans += itemA * itemB
    }

    return ans
}

print(solution([1,4,2],[5,4,4]))
print(solution([1,2],[3,4]))
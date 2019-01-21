import heapq

def solution(scoville, K):
    heap = []
    
    for s in scoville:
        heapq.heappush(heap, s)
    
    answer = 0
    while len(heap) > 0:
        #print(heap)
        if heap[0] >= K:
            return answer
        firstLowScoville = heapq.heappop(heap)
        if heap != []:
            nextLowScoville = heapq.heappop(heap)
            heapq.heappush(heap, firstLowScoville + (nextLowScoville * 2))
        answer +=1    
    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))
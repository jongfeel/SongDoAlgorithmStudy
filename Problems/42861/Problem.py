def findRoot(graph, node):
    if graph[node] != node:
        graph[node] = findRoot(graph, graph[node])
    return graph[node]

def solution(n, costs):
    # initialize graph: set to root node for each node
    graph = [i for i in range(n)]
    # sort by cost
    costs = sorted(costs, key=lambda costs: costs[2])
    
    answer = 0
    for cost in costs:
        # python 신박한 문법 중 하나
        # start=cost[0], end=cost[1], weight=cost[2]
        start, end, weight = cost
        start = findRoot(graph, start)
        end = findRoot(graph, end)
        if start != end:
            # connect node
            graph[start] = end
            answer += weight
            
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

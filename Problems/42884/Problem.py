def solution(routes):
    answer = 0
    # "out" point ascending order sort
    routes = sorted(routes, key=lambda route: route[1])
    #print(routes)
    
    while True:
        # Set up camera point of last out point route value
        cameraPoint = routes[0][1]
        answer += 1
        # Check out "out" point for each routes and remove it
        routes = [route for route in routes if cameraPoint < route[0]]
        #print(routes)
        if len(routes) == 0:
            break
        
    return answer
#6
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))

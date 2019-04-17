def solution(str1, str2):
    
    # define set(집합)
    setA, setB = [], []
    
    # make set two characters
    for i in range(0, len(str1) - 1):
        twochar = str1[i] + str1[i+1]
        #print(twochar)
        if twochar.isalpha() == True:
            setA.append(twochar.lower())
    #print(setA)
    
    for i in range(0, len(str2) - 1):
        twochar = str2[i] + str2[i+1]
        #print(twochar)
        if twochar.isalpha() == True:
            setB.append(twochar.lower())
    #rint(setB)
    
    # get union and intersection
    setA_copy = setA.copy()
    setB_copy = setB.copy()
    union = []
    for a in setA_copy:
        if a in setB_copy:
            #print(a)
            setB_copy.remove(a)
    union = setA_copy + setB_copy
    print(union)
    
    setA_copy = setA.copy()
    setB_copy = setB.copy()    
    intersection = []
    for a in setA_copy:
        if a in setB_copy:
            #print(a)
            intersection.append(a)
            setB_copy.remove(a)
    
    print(intersection)
    
    unionCount = len(union)
    intersectionCount = len(intersection)
    
    #JaccardSimilarity
    if unionCount == 0:
        return 65536
    return (int)(intersectionCount / unionCount * 65536)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "	e=m*c^2"))
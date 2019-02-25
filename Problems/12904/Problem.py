def solution(s):
    answer = 0
    
    index = 0
    length = len(s)
    while index != length:
        index += 1
        for innerIndex in range(0, index):
            # length + 1 - index + innerIndex means to char count
            #print(s[innerIndex:length+1-index+innerIndex])
            palindrome_candidate = s[innerIndex:length+1-index+innerIndex]
            if palindrome_candidate == palindrome_candidate[::-1]:
                return len(palindrome_candidate)
            
    return answer

print(solution("abcdcba"))
print(solution("abacde"))
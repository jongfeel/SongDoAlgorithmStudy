def solution(s):
    answer = ""
    for word in s.split(" "):
        word = word.lower()
        if word != '' and word[0].isalpha():
            word = word.title()
        #print(word)
        answer += word + " "

    return answer[:-1]

print(solution("3people unFollowed me"))
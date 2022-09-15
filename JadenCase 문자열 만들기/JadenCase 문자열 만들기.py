def solution(s):
    answer = ''
    first_word = True
    for c in s:
        if c == ' ':
            answer += ' '; first_word = True
        else:
            if first_word:
                if c.isalpha():
                    answer += c.upper()
                else:
                    answer += c
                
                first_word = False
                
            else: answer += c.lower()
    return answer

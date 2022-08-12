def solution(s):
    answer = []
    for n in sorted(s[2:-2].split('},{'), key=len):
        tmp = set(map(int,n.split(','))) - set(answer)
        answer.append(int(list(tmp)[0]))
    
    return answer

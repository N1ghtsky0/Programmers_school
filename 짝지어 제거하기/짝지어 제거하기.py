def solution(s):
    tmp= [0]
    for c in s:
        if c == tmp[-1]: tmp.pop()
        else: tmp.append(c)
    return int(tmp==[0])

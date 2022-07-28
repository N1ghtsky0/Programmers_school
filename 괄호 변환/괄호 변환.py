def solution(p):
    answer = ''
    if p == '': return answer
    tmp = 0; idx = 0
    for i in p:
        if i == '(': tmp += 1
        else: tmp -= 1
        if tmp == 0: break
        idx += 1
    u, v = p[:idx + 1], p[idx + 1:]
    if checking(u): answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')' + R(u[1:len(u)-1])
    return answer

def R(u):
    result = ['(' if n == ')' else ')' for n in u]
    result = ''.join(result)
    return result

def checking(p):
    result = []; result_str = True; tmp = 0
    for n in p:
        if n == '(': 
            result.append(n)
            tmp += 1
        else:
            tmp -= 1
            try:
                result.pop()
            except:
                result_str = False
                break
    if tmp != 0: result_str = False
    return result_str

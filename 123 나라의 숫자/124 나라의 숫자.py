def solution(n):
    answer = ''
    word124 = ['1', '2', '4']
    k = 0
    while 1:
        Sn = 3 * (3**k - 1) / 2
        if Sn >= n: break
        k += 1
        
    idx = int(n - 3 * (3**(k-1) - 1)  // 2 - 1)
    
    for i in range(int(k-1), -1, -1):
        answer += word124[int(idx // (3 ** i))]
        idx %= 3 ** i
        
    return answer

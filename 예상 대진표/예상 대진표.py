def solution(n,a,b, R=0):
    if a == b: return R
    return solution(n, (a+1)//2, (b+1)//2, R+1)

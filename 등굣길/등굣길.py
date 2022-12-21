dp = {}
def solution(m, n, puddles, state=[1, 1]):
    answer = 0
    
    if state == [m, n]: return 1
    elif state in puddles: return 0

    try:
        return dp[tuple(state)]
    except:
        if state[0] == m:
            dp[tuple(state)] = solution(m, n, puddles, [state[0], state[1]+1])
        elif state[1] == n:
            dp[tuple(state)] = solution(m, n, puddles, [state[0]+1, state[1]]) 
        else:
            dp[tuple(state)] = solution(m, n, puddles, [state[0], state[1]+1]) + solution(m, n, puddles, [state[0]+1, state[1]])
        answer += dp[tuple(state)]
        return answer % 1000000007

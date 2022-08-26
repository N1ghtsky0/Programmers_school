def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(1, len(citations) + 1):
        if i <= citations[i-1]: answer += 1
        else: break
    return answer

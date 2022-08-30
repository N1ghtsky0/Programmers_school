def solution(prices):
    n = len(prices)
    answer = [0] * n
    maintain = []
    for idx, p in enumerate(prices):
        for i in maintain.copy():
            answer[i] += 1
            if prices[i] > p: maintain.pop()
        maintain.append(idx)
    return answer

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    while heap[0] < K:
        if len(heap) <= 2:
            if len(heap) == 2:
                if heap[0] + heap[1]*2 >= K:
                    return answer + 1
            return -1
        s1 = heapq.heappop(heap)
        s2 = heapq.heappop(heap)
        heapq.heappush(heap, s1+s2*2)
        answer += 1

    return answer

from collections import deque

def solution(cards1, cards2, goal):
    Q1 = deque(cards1)
    Q2 = deque(cards2)
    
    for target in goal:
        if len(Q1) != 0 and target == Q1[0]:
            Q1.popleft()
        elif len(Q2) != 0 and target == Q2[0]:
            Q2.popleft()
        else:
            return "No"
    return "Yes"

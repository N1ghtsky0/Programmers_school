def solution(progresses, speeds):
    answer = []
    days = []
    for progress, speed in zip(progresses, speeds):
        day = (100 - progress) // speed
        if (100 - progress) % speed > 0: day += 1
        days.append(day)
    count = 0
    tmp = 0
    for idx in range(len(progresses)):
        if days[tmp] >= days[idx]:
            print('count')
            count += 1
        else:
            tmp = idx
            print('reset')
            answer.append(count)
            count = 1
    answer.append(count)
    return answer

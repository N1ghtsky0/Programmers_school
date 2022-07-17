def solution(record):
    answer = []
    name = {}
    for i in record:
        if list(map(str, i.split()))[0] == 'Enter' or list(map(str, i.split()))[0] == 'Change':
            name[list(map(str, i.split()))[1]] = list(map(str, i.split()))[2]
    for i in record:
        if list(map(str, i.split()))[0] == 'Enter':
            answer.append(name[list(map(str, i.split()))[1]]+'님이 들어왔습니다.')
        elif list(map(str, i.split()))[0] == 'Leave':
            answer.append(name[list(map(str, i.split()))[1]]+'님이 나갔습니다.')
    return answer

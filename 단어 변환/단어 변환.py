from collections import deque

def solution(begin, target, words):
    answer = 0
    word_len = len(words[0])

    if target not in set(words):
        return 0

    checked = {word: False for word in words}

    BFS = deque([begin])

    while BFS:
        l = len(BFS)
        for i in range(l):
            begin = BFS.popleft()
            for word in words:  # 모든 단어들에 대해서
                if not checked[word]:   # 한번 검사한 적 업는 단어일 때
                    tmp = 0
                    for idx in range(word_len):
                        if begin[idx] != word[idx]: tmp += 1    # 중복도 검사
                    if tmp == 1:    # 하나의 철자만 다르다면
                        if word == target: return answer + 1    # 그 단어가 목표 단어일 때 결과 반환

                        checked[word] = True    # 검사한 단어 리스트에 추가
                        BFS.append(word)    # 검사해야할 리스트에 추가
        answer += 1
    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4

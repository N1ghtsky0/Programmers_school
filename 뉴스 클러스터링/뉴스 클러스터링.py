def solution(str1, str2):
    answer = 0
    str1_set, str2_set = make_set(str1), make_set(str2)
    n = len(str1_set) + len(str2_set)
    intersection = 0
    if len(str1_set) <= len(str2_set):
        for item in str1_set:
            if item in str2_set:
                idx = str2_set.index(item)
                str2_set = str2_set[:idx] + str2_set[idx+1:]
                intersection += 1
    else:
        for item in str2_set:
            if item in str1_set:
                idx = str1_set.index(item)
                str1_set = str1_set[:idx] + str1_set[idx+1:]
                intersection += 1
    if intersection == 0:
        if n - intersection != 0: answer = 0
        else:answer = 1
    else: answer = intersection / (n - intersection)
    return int(answer * 65536)

def make_set(s):
    s_set = []
    for i in range(1, len(s)):
        if s[i-1].isalpha() and s[i].isalpha():
            s_set.append(s[i-1].upper()+s[i].upper())
    return s_set

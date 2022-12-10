def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        sk_tree = ''
        for sk in skill_tree:
            if sk in skill: sk_tree += sk
        if sk_tree == '' or (sk_tree in skill and skill[0] == sk_tree[0]): answer += 1
    return answer

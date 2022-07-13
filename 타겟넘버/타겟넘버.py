def solution(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])

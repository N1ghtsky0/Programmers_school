R = []
def solution(numbers):
    answer = 0
    for n in range(1, len(numbers)+1):
        make_all_number(n, numbers)
    for num in list(set(R)):
        isPrime = True
        if num < 2: isPrime=False
        else:
            for i in range(2, int(num**(1/2)+1)):
                if num % i == 0: 
                    isPrime=False; break
        if isPrime: answer += 1
    return answer

def make_all_number(n, numbers, result = ''):
    if n == 0:
        R.append(int(result))
        return
    for idx, num in enumerate(numbers):
        make_all_number(n-1, numbers[:idx]+numbers[idx+1:], result+num)

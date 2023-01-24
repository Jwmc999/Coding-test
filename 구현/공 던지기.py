def solution(numbers, k):
    if (len(numbers)/2) >=k:
        n = len(numbers) //2
    else:
        n = k - len(numbers)//2 + 1
    numbers = numbers * n
    answer = numbers[2*k-2]
    return answer

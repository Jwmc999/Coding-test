def solution(my_string, num1, num2):
    lst = []
    lst[:0] = my_string
    lst[num1], lst[num2] = lst[num2], lst[num1]
    answer = ''.join(lst)
    return answer

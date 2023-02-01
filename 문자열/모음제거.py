import re
def solution(my_string):
    answer = re.sub(r'[aeiou]', '', my_string)
    return answer

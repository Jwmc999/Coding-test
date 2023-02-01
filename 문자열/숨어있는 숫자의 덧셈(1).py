import re
def solution(my_string):
    nums = re.sub(r'[a-zA-Z]','',my_string)
    nums = [int(n) for n in nums]
    answer = sum(nums)
    return answer

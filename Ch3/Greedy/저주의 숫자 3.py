# 배열 문제
# 3의배수 , 3이 들어간 숫자는 건너 뛰고 계산
def three(q, m, n, cnt):
    if (m % 3 == 0) or ('3' in str(m)):
        cnt += 1
        q.remove(m)
        q.append(n+cnt)
        return three(q, n+cnt, n, cnt)
    else:
        return q, cnt

def solution(n):
    queue = [i for i in range(1, n+1)]
    cnt = 0
    for m in range(1, n+1):
        queue, cnt = three(queue, m, n, cnt)
    answer = queue[-1]
    return answer
  
# def solution(n):
#     answer = 0
#     for _ in range(n):
#         answer += 1
#         while answer % 3 == 0 or '3' in str(answer):
#             answer += 1
#     return answer

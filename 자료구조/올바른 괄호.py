def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ")" and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) > 0:
        return False
    else:
        return True

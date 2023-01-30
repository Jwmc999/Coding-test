# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

q = int(sys.stdin.readline())

queries = []
for _ in range(q):
    queries.append(sys.stdin.readline().strip('\n'))
    
tmp = []
for q in queries:
    if ' ' in q:
        tmp.append(q.split(' ')[-1])
    elif q == '2':
        tmp.pop(0)
    else:
        print(tmp[0])

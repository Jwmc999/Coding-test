# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
Q = int(sys.stdin.readline())

ops = []
for i in range(Q):
    ops.append(sys.stdin.readline().strip('\n'))

tmp = ''
undo = []
for o in ops:
    if o[0] == '1':
        undo.append(tmp)
        tmp += o[2:]
    elif o[0] == '2':
        undo.append(tmp)
        tmp = tmp[:-1*int(o[2:])]
    elif o[0] == '3':
        print(tmp[int(o[2:])-1])
    else:
        tmp = undo[-1]
        undo.pop(-1)

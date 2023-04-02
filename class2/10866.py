# [실버4] 덱
import sys
from collections import deque

queue = deque()

N = int(sys.stdin.readline())
for _ in range(N):
    command = str(sys.stdin.readline())
    if command[0] == 's':
        print(len(queue))
    elif command[0] == 'e':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'f':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'b':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif command[:3] == "pop":
        if command[4] == 'f':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        else:
            if queue:
                print(queue.pop())
            else:
                print(-1)
    else:
        _, x = command.split()
        if command[5] == 'f':
            queue.appendleft(int(x))
        if command[5] == 'b':
            queue.append(int(x))
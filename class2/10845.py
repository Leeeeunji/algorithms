# [실버4] 큐
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
    elif len(command) == 4:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    else:
        _, x = command.split()
        queue.append(int(x))
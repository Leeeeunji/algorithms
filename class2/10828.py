# [실버4] 스택
import sys
# 반복문 안에 input()이 들어갈 시 sys.stdin.readline()으로 바꾸기
N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    command = str(sys.stdin.readline()) 
    if command[0] == 's':
        print(len(stack))
    elif command[0] == 'e':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 't':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif len(command) == 4:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        _, x = command.split()
        stack.append(int(x))
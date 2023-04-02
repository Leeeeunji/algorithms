# [실버2] 스택 수열
# 직접 쓰면서 이해해보자.
# 체계적으로 잘 나누어 생각하는 버릇을 기르자.

N = int(input())
li = []
for _ in range(N):
    li.append(int(input())) # 2 4 3 1

temp = 0 # 현재 얼마까지 push했는지
stack = [] 
to_print = []
res_len = 0 # 지금까지 만들어진 수열 길이
stop = -1

for i in range(N): # i = 0 1 2 3, li[i]: 2 4 3 1
    if stop == 1:
        break
    if res_len == N:
        break
    while li[i] > temp: # push
        temp += 1
        stack.append(temp)
        to_print.append('+')
        # print(stack)
        # print("temp:", temp)
    while li[i] < temp: # pop until the target appears
        pop = stack.pop()
        to_print.append('-')
        # print(stack)
        if pop > li[i]:
            stop = 1
            break
        elif pop == li[i]:
            res_len += 1
            break
        
    if li[i] == temp and stack: # pop the target & jump to next li
        res_len += 1
        stack.pop()
        to_print.append('-')
        # print(stack)
        # print("temp:", temp)
        continue
        
if stop == 1:
    print("NO")
else:
    for i in to_print:
        print(i)
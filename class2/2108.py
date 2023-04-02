# [실버 3] 통계학
from collections import Counter

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

counter = dict(Counter(arr))
counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))

max_key_arr = []
num = 0
max_key_arr.append(counter[-1][0])
max_count = counter[-1][1]

for i in range(len(counter)-2, -1, -1):
    if counter[i][1] == max_count:
        max_key_arr.append(counter[i][0])
        num += 1
    else:
        break
        

print(round(sum(arr)/N))

print(arr[N//2])
if num >= 1:
    print(max_key_arr[-2])
else:
    print(max_key_arr[-1])
print(arr[-1] - arr[0])
# [실버5] 나이순 정렬

N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(input().split()))

arr = sorted(arr, key = lambda x: int(x[0]))

for i in range(N):
    print(arr[i][0], arr[i][1])
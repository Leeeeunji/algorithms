# [실버 4] 수 찾기
# 연산 수가 10억 회 이상이면 이진탐색으로 바로 ㄱㄱ

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
x_list = list(map(int, input().split()))

for x in x_list:
    start, end = 0, N-1
    exist = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            exist = 1
            break
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    print(exist)
        
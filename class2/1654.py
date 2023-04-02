# [실버2] 1654. 랜선 자르기
# 이분탐색을 몰라서 헤맸던 문제

K, N = map(int, input().split())
li = []
for i in range(K):
    li.append(int(input()))

start = 1
end = sum(li)//N

while start <= end:
    mid = (start + end) // 2
    num = 0
    for i in li:
        num += i//mid
    if num >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
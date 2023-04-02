# [실버2] 나무 자르기 
# pypy3로 돌리니까 돌아감...
# 간단한 코드 (반복 없이 짧은 코드): 파이썬이 메모리, 속도 측에서 유리
# 반복 등이 많은 복잡한 코드: PyPy3이 속도 면에서 우세
#   이유: pypy3에서는 자주 쓰이는 코드를 캐싱하는 기능이 있음

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end: 
    mid = (start + end) // 2
    temp_m = 0
    for i in tree:
        if i > mid:
            temp_m += (i - mid)
    if temp_m >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
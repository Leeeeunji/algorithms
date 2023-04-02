# [실버 5] 영화감독 숌
# 무조건 복잡하게 생각하지 말고,
# 반복 횟수 계산하고, 단순하게 할 수 있으면 하면 됨
# 너무 어렵게 봐서 오히려 오래 걸렸던 문제

N = int(input())

num = 665
count = 0

while True:
    num += 1
    if '666' in str(num):
        count += 1
    if count == N:
        print(num)
        break
    
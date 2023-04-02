# [브론즈 1] 이항계수 구하기

import itertools

N, K = map(int, input().split())
print(len(list(itertools.combinations(range(N), K))))
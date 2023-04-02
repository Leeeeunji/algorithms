# [브론즈 3] ACM 호텔
T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    if n % h == 0:
        room = h
        floor = n // h
    else:
        room = n % h
        floor = n // h + 1

    print(room * 100 + floor)
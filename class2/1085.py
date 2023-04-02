# 1085. 직사각형에서 탈출
x, y, w, h = list(map(int, input().split()))

minimum = min(x, y, w-x, h-y)

print(minimum)
# 1018번 [실버4] 체스판 다시 칠하기

# (세로, 가로): (n, m)
n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
change_B = [[0] * (m-7) for _ in range(n-7)]
change_W = [[0] * (m-7) for _ in range(n-7)]

for i in range(n-7):
    for j in range(m-7):
        criteria = arr[i][j]
        for a in range(8):
            for b in range(8):
                if (a+b)%2==0:
                    if criteria != arr[i+a][j+b]:
                        change_B[i][j] += 1
                    else:
                        change_W[i][j] += 1
                else:
                    if criteria == arr[i+a][j+b]:
                        change_B[i][j] += 1
                    else:
                        change_W[i][j] += 1
                    
min = 10e9

for array in change_B:
    for x in array:
        if x < min:
            min = x
for array in change_W:
    for x in array:
        if x < min:
            min = x

print(min)
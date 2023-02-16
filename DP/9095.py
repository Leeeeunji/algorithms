T = int(input())
test = []

for i in range(T):
    test.append(int(input()))

dp = [0] * 12
dp[2] = 1
dp[3] = 3
def topDown(N:int) -> int:
    if N==1:
        return 1
    if N==2:
        return 2
    if N==3:
        return 4
    
    # 메모해둔 값일 경우
    if dp[N] != 0:
        return dp[N]
    dp[N] = int(topDown(N-1)) + int(topDown(N-2)) + int(topDown(N-3))
    return dp[N]

for i in test:
    print(int(topDown(i)))
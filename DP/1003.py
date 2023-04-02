n = int(input())
T = []
for i in range(n):
    T.append(int(input()))

dp = [0] * 41
cnt0 = [0] * 41
cnt1 = [0] * 41

dp[0] = 0
dp[1] = 1
cnt0[0] = 1
cnt1[1] = 1

def fibonacci(n:int) -> int:
    if n==0:
        return 0
    elif n==1:
        return 1
    elif dp[n] != 0:
        return dp[n]
    else:
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
        cnt0[n] = cnt0[n-1] + cnt0[n-2]
        cnt1[n] = cnt1[n-1] + cnt1[n-2]
        return dp[n]

for t in
    fibonacci(t)
    print(str(cnt0[t]) + " " + str(cnt1[t]))

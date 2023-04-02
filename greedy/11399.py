# [실버 4] ATM

N = int(input())
arr = list(map(int, input().split()))

# arr[0]*5 + arr[1]*4 + arr[2]*3 + arr[3]*2 + arr[4]*1
arr.sort()
sum = 0
for i in range(N):
    sum += arr[i] * (N-i)
    
print(sum)
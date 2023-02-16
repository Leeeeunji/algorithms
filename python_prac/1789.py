S = int(input())
sum = 0
for i in range(1, S+1):
    sum = i + sum
    if sum > S:
        print(i-1)
        break
    elif sum == S:
        print(i)
        break
        
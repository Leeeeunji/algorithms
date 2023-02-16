n, m = input().split()
n = int(n)
m = int(m)

minimum = min(m, n)
maximum = max(m, n)
ret = minimum*(maximum-1) + minimum-1

print(ret)
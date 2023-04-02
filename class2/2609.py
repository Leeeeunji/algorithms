# [브론즈 1] 최대공약수와 최소공배수
import math

x, y = map(int, input().split())
gcd = math.gcd(x, y)
lcm = x*y // gcd
print(gcd)
print(lcm)
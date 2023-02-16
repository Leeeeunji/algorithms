N = int(input())
x = N
cycle = 0

while True:
    cycle += 1
    if N<10:
        second = N
        new = second*10+second
    
    else:
        first = N // 10 # 10
        second = N % 10 # 1
        new = second * 10 + (first + second) % 10
    
    if new == x: break
    N = new

print(cycle)
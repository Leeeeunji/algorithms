"""
# 알파벳 a~z를 입력받고, a부터 입력문자까지 차례대로 출력하기
for i in range(ord(input()) - ord('a') + 1):
    print(chr(ord('a') + i), end=' ')
    
# 0이 입력되기 전까지 계속 입력받기
while bool(int(input())):
    continue

# 정수 1개 입력받아 1부터 그 수까지 짝수의 합 구하기
sum = 0
for i in range(int(input()) + 1):
    if not i%2:
        sum += i
print(sum)
 
# 6078
while True:
    a=input()
    print(a)
    if a == 'q': break
    
# 6079
sum = 0
for i in range(int(input())+1):
    sum += i
print(sum)

# 6081
x = int(input(), 16)
for i in range(1, 16):
    print('%X'%x, "*", '%X'%i, "=", '%X'%(x*i))

# 6082
for i in range(1, int(input())+1):
    if (i%10)%3==0 and i%10!=0:
        print('X', end=' ')
    else:
        print(i, end=' ')

# 6092
n = int(input())
num = input().split()
    
l = [0] * 24
for i in num:
    l[int(i)] += 1
    
print(l[1:])

# 6095
d = [[0]*21]*21 # 이렇게 하면 오류 발생
d = [[0 for col in range(21)] for row in range(21)] # 2차원 리스트 만들땐 꼭 이렇게!
for i in range(1,21):
    for j in range(1,21):
        print(d[i][j], end=' ')
    print()


n = int(input())
for i in range(n):
    x,y=input().split()
    d[int(x)][int(y)] = 1


for i in range(1,21):
    for j in range(1,21):
        print(d[i][j], end=' ')
    print()
    
"""
# 6096
l = [[0 for col in range(20)] for row in range(20)]
for i in range(20):
    l[i] = input().split()

n = int(input())

for a in range(n):
    x, y = input().split()
    for i in range(20):
        if l[y][i]==0:
            l[y][i] = 1
        else:
            l[y][i] = 0
    for i in range(20):
        if l[i][x]==0:
            l[i][x] = 1
        else:
            l[i][x] = 0
        
for i in range(20):
    for j in range(20):
        print(l[i][j], end=' ')
    print()
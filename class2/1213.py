# [실버3] 팰린드롬 만들기
from collections import Counter

name = input()
counter = dict(Counter(name))

even = []
odd = ''
dont = 0
result = []


for key, value in counter.items(): # dict 자료형 반복 시
    if value % 2 == 1:
        if odd != '':
            dont = 1
            break
        odd = key
        for _ in range(value//2):
            even.append(key)
    else:
        for _ in range(value//2):
            even.append(key)

even.sort()

if dont == 1:
    print("I'm Sorry Hansoo") 
elif odd != '':
    for i in even:
        print(i, end='')
    print(odd, end='')
    result += odd
    for i in even[::-1]:
        print(i, end='')
else:
    for i in even:
        print(i, end='')
    for i in even[::-1]:
        print(i, end='')

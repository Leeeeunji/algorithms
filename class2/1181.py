# 1181. 단어 정렬

N = int(input())

li = []

for i in range(N):
    li.append(input())

li = list(set(li))
li = sorted(li, key=lambda x: (len(x), x))

for i in li:
    print(i)
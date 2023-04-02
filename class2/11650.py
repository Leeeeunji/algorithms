# 11650. 좌표 정렬하기

N = int(input())

list = []

for i in range(N):
    list.append(tuple(map(int, input().split())))

# key 두 개를 이용하여 정렬 가능!
sorted_list = sorted(list, key=lambda x:(x[0], x[1]))

for item in sorted_list:
    print(f"{item[0]} {item[1]}")
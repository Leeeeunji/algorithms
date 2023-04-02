# 삽입 정렬

arr = [0, 1, 9, 7, 3, 5, 6, 2, 4, 8]

for i in range(1, len(arr)):
    temp = arr[i]
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            continue
        
print(arr)
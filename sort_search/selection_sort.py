# 선택 정렬

arr = [0, 1, 9, 7, 3, 5, 6, 2, 4, 8]

for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i] # 스왑 연산
        
print(arr)
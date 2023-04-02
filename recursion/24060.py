unsorted = [21, 10, 12, 20, 25, 13, 15, 22]
sorted = []

def merge(list, left, mid, right):
    i = left
    j = mid + 1
    k = left
    while(i<=mid and j <= right):
        if(list[i] <= list[j]):
            sorted[k++] = list[i++]
            
        
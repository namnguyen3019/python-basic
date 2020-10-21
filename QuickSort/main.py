def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p)
        quickSort(arr, p+1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j: return j # why
        arr[i], arr[j] = arr[j], arr[i]

if __name__=="__main__":
    arr = [0,9,7,4,5,2,1,5]
    quickSort(arr, 0, len(arr)-1)
    print(arr)
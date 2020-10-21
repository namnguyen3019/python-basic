def selectionSort(arr):

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        #Swap
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp

if __name__=="__main__":
    arr = [0,2,3,4,1,1]
    selectionSort(arr)
    print(arr)
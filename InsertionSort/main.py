def insertionSort(arr):
   for i in range(1, len(arr)):
       key = arr[i]
       j = i - 1
       while j >= 0 and key < arr[i]:
           arr[j+1] = arr[j]
           j -= 1
       arr[j+1] = key

if __name__=="__main__":
    arr = [0, 1, 3 , 2]
    insertionSort(arr)
    print(arr)

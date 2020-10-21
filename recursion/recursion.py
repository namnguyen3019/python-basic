# Merge Sort: 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2 # Find the middle number
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L) # Merge Sort for the Left array
        mergeSort(R) # Merge SOrt for the R array

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = R[j]
                j += 1
            else:
                arr[k] = L[i]
                i += 1
            k += 1
        # Checking if element left in L and R
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i])

if __name__ == '__main__': 
    arr = [1, 2]  
    mergeSort(arr)
    printList(arr)
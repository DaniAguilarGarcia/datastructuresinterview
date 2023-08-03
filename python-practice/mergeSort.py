
def mergeSort(array):
    if len(array) > 1:
        #r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[l:]

        #sort the two halvs
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        #until we reach the end of either L or M, pick larger among
        #elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[I] < M[J]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        #when we run out of element in either L or M
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
#print array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
#driver program

if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
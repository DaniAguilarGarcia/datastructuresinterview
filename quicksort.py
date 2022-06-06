#quick sort algorithm
#divide and conquer algorithm
#running time o(n^2) worst case, and o(n*log(n)) best and average case
#when is quick sort inpractical

#choose pivot element (Usually last or random)
#stores elements less than pivot is left subarray, 
#stores elements greater than pivot in right subarray
#call quicksort on both subarray
# 22 11 88 66 55 77 33 44

def quicksort(arr, left, right): #lefet and right are two indexes
    if left < right: #the array contains more than 2 elements
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1) # all elements less than pivot
        quicksort(arr, partition_pos + 1, right) # all elements greater than pivot element

def partition(arr, left, right):
    i = left #moves to the right
    j = right - 1 #moves to the left
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot: # while i is not at the end of the array and element at index i is less than pivot
            i += 1 #we increase i
        while j > left and arr[j] >= pivot:
            j -= 1 # j moves to the left
        if i < j: #do this elements cross yet? if not, we swap
            arr[i], arr[j] = arr[j], arr[i] #swap
    if arr[i] > pivot: 
        arr[i], arr[right] = arr[right], arr[i] # we swap when they cross

    return i

arr = [22 , 11, 88, 66 , 55, 77 , 33, 44]
print(arr)
quicksort(arr, 0, len(arr) - 1)
print(arr)

#find the partition position https://www.programiz.com/dsa/quick-sort

def partition(array, left, right):
#choose the right most element as pivot
    pivot = array[right]
    #pointer for greater element
    i = left - 1
    #traverse through all elements , compare each element with pivot
    for j in range(left,right):
        if array[j] <= pivot:
            #if element smaller than pivot is found, swap it with the greater element pointed by i
            i = i + 1
            #swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
        #swap the pivot element with the greater element specified by i
        (array[i+1], array[right]) = (array[right], array[i+1])
    #return the position from where the partition is done
    return i + 1

#function to perform quickSort
def quickSort(array, left, right):
    if left < right:
        #find the pivot element so that element smaller than pivot are on the left and element greater than pivot are on the right
        pi = partition(array, left, right)
        #recursive call on the left of the pivot
        quickSort(array, left, pi - 1)
        #recursive call on the right of the pivot
        quickSort(array, pi + 1, right)





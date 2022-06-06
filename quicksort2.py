#quick sort works, recursive method
#pivot is what we use to compare 
#left partition x < pivot
#right partition x> pivot
#performance depends on pivot selection
#pivot can be the median of 3. first, last and middle
#randomly chosen pivots ensure O(n log n)
#https://www.geeksforgeeks.org/python-program-for-quicksort/


# low - > starting index. high --> ending index
# quickSort(arr[], low, high)
#until starting index is lesser than ending index
#if (low < high)

#pi is partitioning index, arr[p] is now at the right place
# pi = partition(arr, low, high)
#before pi
#quickSort(arr, low, pi - 1);
#after pi
#quickSort(arr, pi + 1, high)

def partition(i, r , nums):
    #last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
        #swaping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swappping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)
        quicksort(pi+1, r, nums)
    return nums




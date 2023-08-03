#sorting the array

def kth_largest(arr, k):
    n = len(arr)
    arr.sort() # o(nlogn)
    return arr[n-k]
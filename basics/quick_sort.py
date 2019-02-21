# built-int list1.sort() sorted(list1) can be used 

def partition(arr, i, j, p):
    left = i
    right = j
    while(left < right):
        while(arr[left] < p):
            left += 1
        while(arr[right] > p):
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    return left

def _quickSort(arr:'list', i:'int', j:'int'):
    if (i<j):
        p = arr[i] # use the first ele as pivot here
        k = partition(arr, i, j, p)
        _quickSort(arr, i, k)
        _quickSort(arr, k+1, j)
    return arr
def quickSort(arr:'list'):
    return _quickSort(arr, 0, len(arr)-1)
# test
if __name__ == '__main__':
    print(quickSort([1, 3, 2]))

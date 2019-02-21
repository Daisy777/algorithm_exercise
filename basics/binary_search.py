# python has build in module implemented for binary search
# import bisect
# bisect.bisect_left
def _binarySearch(begin:'int', end:'int', arr:'list', ele) -> 'int':
    if begin > end:
        return -1
    if begin == end:
        return begin if arr[begin] == ele else -1
    middle = (begin+end)//2
    if arr[middle] == ele:
        return middle
    if arr[middle] < ele:
        return _binarySearch(middle+1, end, arr, ele)
    return _binarySearch(begin, middle, arr, ele)

def binarySearch(arr:'list', ele) -> 'int':
    return _binarySearch(0, len(arr)-1, arr, ele)

# test
if __name__ == '__main__':
    print(binarySearch([1, 2, 3], 1.5))
    print(binarySearch([1, 2, 3], 3))


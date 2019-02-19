
def _merge_sort(arr:'list'):
    if len(arr) <= 1:
        return arr
    begin = 0
    end = len(arr)-1
    middle = (begin+end)//2
    first = _merge_sort(arr[begin:middle+1])
    second = _merge_sort(arr[middle+1:end+1])
    # merge
    ptr1 = begin
    ptr2 = middle+1
    ptr = 0
    while(ptr1<middle+1 and ptr2<end+1):
        if first[ptr1] < second[ptr2-middle-1]:
            arr[ptr] = first[ptr1]
            ptr1 += 1
        else:
            arr[ptr] = second[ptr2-middle-1]
            ptr2 += 1
        ptr += 1
    # print(ptr1, ptr2)
    while(ptr1 < middle+1):
        arr[ptr] = first[ptr1]
        ptr1 += 1
        ptr += 1
    while(ptr2 < end+1):
        arr[ptr] = second[ptr2-middle-1]
        ptr2 += 1
        ptr += 1

    return arr

# test
if __name__ == '__main__':
    print(_merge_sort([1, 3, 2]))
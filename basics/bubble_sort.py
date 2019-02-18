def bubble_sort(arr:'list'):
    # inplace sort
    for i in range(len(arr)-1):
        for j in range(len(arr)-1, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr
    
# test
if __name__ == '__main__':
    print(bubble_sort([1, 3, 2, 4]))
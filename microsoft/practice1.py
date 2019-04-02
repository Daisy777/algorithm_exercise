'''
Author: ZHAO Zinan
Created: 02. April 2019

1) If the elements of index i and (i+1) are equal then, double the value at index i
and replace the element at index (i+1) with 0. 
2) If the element at index i is 0, then ignore it.
3) Any number (element in an array) must be modified only once.
4) At the end, shift all the zeros (0s) to the right of the array and remaining
nonzeros to the left of the array.
Example: 
Input: 2 2 0 4 0 8
Output: 4 4 8 0 0 0
Input: 2 2 0 4 0 2
Output: 4 4 2 0 0 0

'''
def shift(arr):
    if not arr:
        return []
    # inplace
    ptr=0
    ptrresult=0
    length = len(arr)

    while(ptr<length-1):
        if arr[ptr] == arr[ptr+1]:
            arr[ptrresult] = arr[ptr]*2
            ptrresult += 1
            ptr += 1
        elif arr[ptr] != 0:
            arr[ptrresult] = arr[ptr]
            ptrresult += 1
        ptr += 1
    
    if ptr < length and arr[-1] != 0:
        arr[ptrresult] = arr[-1]
        ptrresult += 1
    while(ptrresult<length):
        arr[ptrresult] = 0
        ptrresult += 1
    return arr


if __name__ == '__main__':
    print(shift([2, 2, 0, 4, 0, 8])) # [4, 4, 8, 0, 0, 0]
    print(shift([]))
    print(shift([0]))
    print(shift([2, 2, 0, 4, 0, 2])) # [4, 4, 2, 0, 0, 0]

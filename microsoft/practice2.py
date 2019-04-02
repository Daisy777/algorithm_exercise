'''
Author: ZHAO Zinan
Created: 02. April 2019

Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
Input: 2 0 3 5 6 1
Output: 4
There was only one test case given which is mentioned above. But I am providing the below one of the sample cases which is an important thing to be noted. It returns -1 because all the
elements after any given element are smaller than it. DO take care of such cases.
Input: 9 8 7 6 5
Output: -1
'''
def index_diff(arr):
    if not arr:
        return -1

    length = len(arr)
    maxarr = [length-1]*length
    minarr = [0]*length

    minarr[0] = arr[0] 
    for i in range(1, length):
        minarr[i] = min(minarr[i-1], arr[i])

    maxarr[length-1] = arr[length-1]
    for i in range(length-2, -1, -1):
        maxarr[i] = max(maxarr[i+1], arr[i])

    print(maxarr, minarr)
    maxdiff = -1;i=0;j=0
    while(i<length and j<length):
        if (maxarr[j] > minarr[i]):
            # print(maxarr[j], arr[minarr[i]])
            maxdiff = max(maxdiff, j-i)
            j += 1
        else:
            i += 1
    return maxdiff

if __name__=='__main__':
    print(index_diff([2, 0, 3, 5, 6, 1])) # 4
    print(index_diff([34, 8, 10, 3, 2, 80, 30, 33, 1])) # 6
    print(index_diff([9, 2, 3, 4, 5, 6, 7, 8, 18, 0])) # 8
    print(index_diff([1, 2, 3, 4, 5, 6])) # 5
    print(index_diff([9, 8, 7])) # -1

    

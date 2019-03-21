'''
Author: ZHAO Zinan
Created: 21. March 2019

944. delete columns to make sorted
''' 
class Solution:
    def minDeletionSize(self, A) -> int:
        if not A or not A[0] or len(A[0]) == 1:
            return 0
        
        converted = list(map(list, zip(*A)))
        totalnum = 0
        for l in converted:
            for index, char in enumerate(l[:-1]):
                if char > l[index+1]:
                    totalnum += 1
                    break
        return totalnum
    
# test
if __name__ == '__main__':
    print(Solution().minDeletionSize(['a', 'b']))# 0
    print(Solution().minDeletionSize(['cba', 'daf', 'ghi']))# 1
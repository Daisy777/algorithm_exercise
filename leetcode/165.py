'''
Author: ZHAO Zinan
Created: 02. March 2019

165. Compare Version Numbers
''' 
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1arr = list(map(int, version1.split('.')))
        version2arr = list(map(int, version2.split('.')))
        lenversion1 = len(version1arr)
        lenversion2 = len(version2arr)
        
        for index in range(min(lenversion1, lenversion2)):
            if version1arr[index] < version2arr[index]:
                return -1
            if version1arr[index] > version2arr[index]:
                return 1
            
        # need to remove all the 0s in the tail
        
        if len(version1arr) > len(version2arr):
            if sum(version1arr[lenversion2:]) ==0:
                return 0
            return 1
        if len(version1arr) < len(version2arr):
            if sum(version2arr[lenversion1:]) == 0:
                return 0
            return -1
        return 0

# test
if __name__ == '__main__':
    print(Solution().compareVersion('0.1', '1.1')) # -1
    print(Solution().compareVersion('1.0', '1')) # 0
    print(Solution().compareVersion('1.0.1', '1')) # 1
    print(Solution().compareVersion('1.01', '1.001')) # 0
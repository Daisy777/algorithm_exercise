'''
Author:    ZHAO Zinan
Created: 01/23/2019

274. H-Index
'''
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse = True)
        for index, ele in enumerate(citations):
            if index+1 <= ele:
                if index<len(citations)-1 and citations[index+1] <= index+1:
                    return index+1
                elif index==len(citations)-1:
                    return len(citations)
        return 0

# test
if __name__ == '__main__':
    print(Solution().hIndex([3, 0, 6, 1, 5])) # 3
    print(Solution().hIndex([1])) # 1
    print(Solution().hIndex([11, 15])) # 2

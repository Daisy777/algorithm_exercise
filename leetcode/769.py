class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return 1
        
        i = 0
        chunk_num = 0
        while (i<len(arr)):
            if (arr[i] == i):
                chunk_num += 1
               
            elif (arr[i] > i):
                # arr[i] should be put in locus arr[i]
                while (arr[i] > i):
                    next_locus = arr.index(max(arr[i:arr[i]+1]))
                    i = arr[i]
                    if (arr[next_locus] > i):
                        i = arr[next_locus]
                    else:
                        break
                chunk_num += 1

            i += 1
                
        return chunk_num


# test
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxChunksToSorted([4, 3, 2, 1, 0])) # 1
    print(solution.maxChunksToSorted([1, 0, 2, 3, 4])) # 4
    print(solution.maxChunksToSorted([0, 1, 3, 5, 4, 2])) # 3
    print(solution.maxChunksToSorted([2, 6, 1, 3, 0, 5, 4])) # 1
    print(solution.maxChunksToSorted([1,4,3,6,0,7,8,2,5])) # 1
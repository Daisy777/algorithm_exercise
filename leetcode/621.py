'''
Author:    ZHAO Zinan
Created: 01-Nov-2018

621. Task Scheduler
https://leetcode.com/problems/task-scheduler/description/
'''

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        counter = dict(Counter(tasks))
        maxLen = max(counter.values())
        maxCnt = len([key for key, value in counter.items() if value == maxLen])
        return max(len(tasks), n*(maxLen-1)+maxLen+maxCnt-1)

# test
if __name__=='__main__':
    solution = Solution()
    print(solution.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2)) # 8

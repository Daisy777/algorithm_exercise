class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])

        result = '/'.join([str(num) for num in nums])

        if len(nums) > 2:
            strlist = result.split('/', 1)
            result = '/('.join(strlist)
            result += ')'

        return result

if __name__ == '__main__':
    print(Solution().optimalDivision([1000, 100, 10, 2]))
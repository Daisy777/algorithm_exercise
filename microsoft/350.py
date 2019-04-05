'''
Author: ZHAO Zinan
Created: 06. April 2019

350. Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
''' 
class Solution:
    def intersect(self, nums1, nums2):
        import collections
        dict1 = collections.defaultdict(int)
        dict2 = collections.defaultdict(int)
        for i in nums1:
            dict1[i] += 1
        for i in nums2:
            dict2[i] += 1
        
        result = []
        for key in dict1:
            result.extend([key]*min(dict1[key], dict2[key]))
        return result

# test
if __name__ == '__main__':
    print(Solution().intersect([1,2,2,1], [2,2])) # 2, 2
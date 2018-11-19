'''
Author:    ZHAO Zinan
Created: 18-Nov-2018

406. Queue Reconstruction by Height
https://leetcode.com/problems/queue-reconstruction-by-height/description/
'''
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # record the height group and its corresponding index
        heightgroup = {}
        for index, person in enumerate(people):
            if person[0] not in heightgroup.keys():
                heightgroup[person[0]] = [index]
            else:
                heightgroup[person[0]].append(index)
        
        keys = sorted(list(heightgroup.keys()), reverse=True)
        reconstructed = []
        
        for index, key in enumerate(keys):
            indexgroup = heightgroup[key]
            elegroup = []
            for index in indexgroup:
                elegroup.append(people[index])
            elegroup.sort(key=lambda x:x[1])
            
            for index, ele in enumerate(elegroup):
                reconstructed.insert(ele[1], ele)
        return reconstructed
                
        
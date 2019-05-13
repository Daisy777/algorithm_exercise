'''
Author:    ZHAO Zinan
Created: 14-May-2019

609. Find Duplicate File in System
'''
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        contents = collections.defaultdict(list)
        for path in paths:
            splitedpath = path.split()
            root = splitedpath[0]
            for file in splitedpath[1:]:
                name, content = file.split('(')
                contents[content].append('/'.join([root, name]))
        return [contents[key] for key in contents if len(contents[key]) > 1]    
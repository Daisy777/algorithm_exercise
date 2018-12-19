'''Author:    ZHAO Zinan
Created: 12/19/2018

388. Longest Absolute File Path
'''
class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        def isFile(name):
            if len(name.split('.')) > 1:
                return True
            return False

        def isDirectory(name):
            if not name.contains('.'):
                return True
            return False

        def tabNum_n_removeTab(name):
            num = 0
            while (name[:1] == '\t'):
                num += 1
                name = name[1:]
            return (num, name)

        inputsplit = input.split('\n')
        length = 0
        stack = []
        largestLen = 0

        for file in inputsplit:
            tabnum, file = tabNum_n_removeTab(file)
            while tabnum < len(stack):
                ele = stack.pop()
                length -= len(ele) 

            if isFile(file):
                # if it is file, no need to put it in 
                largestLen = max(largestLen, length+len(file)+len(stack))
                
            else:
                stack.append(file)
                length += len(file) 

        return largestLen

# test
if __name__ == '__main__':
    print(Solution().lengthLongestPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')) # 32
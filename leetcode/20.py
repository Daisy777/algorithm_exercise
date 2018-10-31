'''
Author:    ZHAO Zinan
Created: 31-Oct-2018

20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        
        stack = []
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
            else:
                if len(stack) != 0: 
                    last = stack.pop()
                else: # more ] ) }
                    return False
                        
                # don't appear as pair
                if last != pair[char]:
                    return False
        
        # more [ ( { 
        return True if len(stack) == 0 else False
                
        
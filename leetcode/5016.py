'''
Author: ZHAO Zinan
Created: 07. April 2019

5016. Remove Outermost Parentheses
''' 
class Solution:
    def removeOuterParentheses(self, S):
        if not S:
            return ''
        result = ''
        stack = []
        leftnum = 0
        rightnum = 0
        for char in S:
            if char != ')':
                stack.append(char)
                leftnum += 1
            else:
                rightnum += 1
                if rightnum == leftnum:
                    rightnum -= 1
                    temp = ''
                    while(leftnum>0):
                        popchar = stack.pop()
                        temp += popchar
                        if popchar == '(':
                            leftnum -= 1
                        elif popchar == ')':
                            rightnum -= 1
    
                    result += temp[:-1][::-1]
                else:
                    stack.append(char)
        
        return result
# test
if __name__ == '__main__':
    print(Solution().removeOuterParentheses("()()")) # ""
    print(Solution().removeOuterParentheses("(()())(())(()(()))")) # "()()()()(())"

                
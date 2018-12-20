'''
Author:    ZHAO Zinan
Created: 12/20/2018

394. Decode String
'''
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        stack = []
        result = ''

        for char in s:
            if char != ']':
                stack.append(char)

            else:
                # letter part
                nextchar = stack.pop()
                letters = ''
                while (nextchar != '['):
                    letters = nextchar + letters
                    nextchar = stack.pop()

                # digit times part - ugly part
                nextchar = stack.pop()
                times = ''
                while (nextchar in digits):
                    times = nextchar + times
                    if len(stack) != 0:
                        nextchar = stack.pop()
                    else:
                        break
                if nextchar not in digits:
                    stack.append(nextchar)

                stack.append(letters*int(times))

        return ''.join(stack)

# test
if __name__ == '__main__':
    print(Solution().decodeString('2[c]')) # cc
    print(Solution().decodeString('2[a]2[c]')) # aacc
    print(Solution().decodeString('2[c2[a]]')) # caacaa
    print(Solution().decodeString('2[aaa2[b2[b]]]3[abc]')) # aaabbbbbbaaabbbbbbabcabcabc

                

        
'''
Author:    ZHAO Zinan
Created: 12/19/2018

482. License Key Formatting
'''
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        groups = S.split('-')
        str = ''.join(groups)
        newgroups = []
        for i in range(len(str)-1, -1, -K):
            if i-K+1 < 0:
                newgroups.append(str[:i+1].upper())
                break
            newgroups.append(str[i-K+1:i+1].upper())

        return '-'.join(list(reversed(newgroups)))

# test
if __name__ == '__main__':
    print(Solution().licenseKeyFormatting('5F3Z-2e-9-w', 4)) # '5F3Z-2E9W'
    print(Solution().licenseKeyFormatting('2-5g-3-J', 2))  # '2-5G-3J'



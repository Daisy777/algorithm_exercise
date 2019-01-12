'''
Author:    ZHAO Zinan
Created: 01/12/2019

524. Longest Word in Dictionary through Deleting
'''
class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        largest_word = ''
        for word in d:
            if len(word) < len(largest_word) or (len(word) == len(largest_word) and word > largest_word):
                continue

            i=0
            j=0

            while(i<len(s) and j<len(word)):
                if(s[i] == word[j]):
                    j+=1
                i+=1

            if j == len(word):
                largest_word = word
        return largest_word

# test 
if __name__ == '__main__':
    print(Solution().findLongestWord('abpcplea', ['ale', 'apple', 'monkey', 'plea']))
    # 'apple'

    print(Solution().findLongestWord('abpcplea', ['a', 'b', 'c']))
    # 'a'

    print(Solution().findLongestWord('bab', ['ba', 'ab', 'a', 'b']))
    # 'ab'
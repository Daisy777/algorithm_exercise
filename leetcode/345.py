'''
Author:    ZHAO Zinan
Created: 01/12/2019

345. Reverse Vowels of a String
'''
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1:
            return s
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        modified_s_list = []
        vowel_loc = []
        for index, char in enumerate(s):
            modified_s_list.append(char)
            if char in vowels:
                vowel_loc.append(index)
                
        
        num_vowel = len(vowel_loc)
        for i in range(num_vowel//2):
            modified_s_list[vowel_loc[i]], modified_s_list[vowel_loc[num_vowel-i-1]] = modified_s_list[vowel_loc[num_vowel-i-1]], modified_s_list[vowel_loc[i]]
        
        return ''.join(modified_s_list)
    # a faster way - two pointers
            
            
        
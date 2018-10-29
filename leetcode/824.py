class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        # if len(S) == 0:
        #     return S
        
        # vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        # strarr = S.split()
        # for i in range(len(strarr)):
        #     if (strarr[i][0] in vowel):
        #         strarr[i] += 'ma'
        #     else:
        #         strarr[i] = strarr[i][1:] + strarr[i][0] + 'ma'
            
        #     strarr[i] += 'a'*(i+1)
            
        # return ' '.join(strarr)

        # use enumerate for faster speed

        if len(S) == 0:
            return S
        
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        strarr = S.split(' ')
        for index, word in enumerate(strarr):
            if (word[0] in vowel):
                strarr[index] += 'ma'
            else:
                strarr[index] = word[1:] + word[0] + 'ma'
            
            strarr[index] += 'a'*(index+1)
            
        return ' '.join(strarr)
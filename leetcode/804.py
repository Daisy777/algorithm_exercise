'''
Author: ZHAO Zinan
Created: 23. February 2019

804. Unique Morse Code Words
''' 
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        wordset = set([])
        for word in words:
            mappingstr = ''
            for char in word:
                mappingstr += mapping[ord(char)-ord('a')]
            wordset.add(mappingstr)
        return len(wordset)
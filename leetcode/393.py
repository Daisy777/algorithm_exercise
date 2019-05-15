'''
Author:    ZHAO Zinan
Created: 15-May-2019

393. UTF-8 Validation 
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
'''
from typing import List 

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return True 
        def binstr(num):
            return bin(num)[2:]

        data = list(map(binstr, data))
        print(data)
        i=0
        while( i< len(data)):
            if len(data[i]) < 8:
                i += 1
                continue 
            elif data[i].startswith('110'):
                for j in range(1):
                    if i+j+1 >= len(data) or len(data[i+j+1]) < 8 or not data[i+j+1].startswith('10'):
                        return False 
                i += 2 
            elif data[i].startswith('1110'):
                for j in range(2):
                    if i+j+1 >= len(data) or len(data[i+j+1]) < 8 or not data[i+j+1].startswith('10'):
                        return False 
                i += 3
            elif data[i].startswith('11110'):
                for j in range(3):
                    if i+j+1 >= len(data) or len(data[i+j+1]) < 8 or not data[i+j+1].startswith('10'):
                        return False 
                i += 4
            else: 
                return False 
        return True 


# test 
if __name__ == '__main__':
    print(Solution().validUtf8([197, 130, 1]))    
    print(Solution().validUtf8([235, 140, 4])) 
    print(Solution().validUtf8([237])) 
    print(Solution().validUtf8([240,162,138,147])) 
        

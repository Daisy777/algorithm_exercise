from typing import List 

class Solution:
    def compress(self, chars: List[str]) -> int:
        front, char, begin = 0, 0, 0
        while (front < len(chars)):
            if chars[front] != chars[begin]:
                chars[char] = chars[begin]
                char += 1
                if front - begin > 1:
                    num = list(str(front-begin))
                    for index, n in enumerate(num):
                        chars[char+index] = n 
                    char = char+len(num)
                begin = front

            if front == len(chars)-1:
                chars[char] = chars[begin]
                char += 1
                if front - begin > 0:
                    num = list(str(front-begin+1))
                    for index, n in enumerate(num):
                        chars[char+index] = n 
                    char = char+len(num)
                begin = front
            front += 1
        print(chars)
        return char

if __name__ == '__main__':
    print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    print(Solution().compress(["a","b"]))
    print(Solution().compress(["a","a","a","b","b","a","a"]))
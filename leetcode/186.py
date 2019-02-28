class Solution:
    def reverseWords(self, str: List[str]) -> None:
        """
        Do not return anything, modify str in-place instead.
        """
        word = False
        start = 0
        finish = 0
        for index, char in enumerate(str):
            if char != " ":
                if not word:
                    word = True
                    start = index
                
            else:
                if word:
                    word = False
                    finish = index
                    self.reverseWord(str, start, finish)
        if word:
            word = False
            finish = len(str)
            self.reverseWord(str, start, finish)
        str.reverse()

        
    def reverseWord(self, str, i, j):
        length = j-i
        for x in range(length//2):
            str[i], str[j-1] = str[j-1], str[i]
            i+=1
            j-=1
        
# test
if __name__ == '__main__':
    print(Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
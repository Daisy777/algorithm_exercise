class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ''
        for i in range(len(s)//(2*k)):
            print(i, k)
            print(s[i*2*k:(2*i+1)*k])
            print(s[i*2*k:(2*i+1)*k][::-1])
            result = ''.join([result, s[i*2*k:(2*i+1)*k][::-1]])
            print(result)
            result = ''.join([result, s[(2*i+1)*k:(2*i+2)*k]])
            print(result)
            
        return result
        
# test
if __name__ == '__main__':
    print(Solution().reverseStr("abcdefg", 2))

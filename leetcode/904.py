class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        if not tree:
            return 0
        stack = []
        currentlen = 0
        maxlen = 0
        last = 0

        for index, fruit in enumerate(tree):
            if stack and fruit == stack[len(stack)-1]:
                currentlen += 1
            elif len(stack) < 2:
                currentlen += 1
                stack.append(fruit)
                last = index
            elif fruit == stack[0]:
                stack[0], stack[1] = stack[1], stack[0]
                currentlen += 1
                last = index  
            else:
                stack.pop(0)
                stack.append(fruit)      
                maxlen = max(currentlen, maxlen)
                currentlen = index-last+1
                last = index  
            
        maxlen = max(currentlen, maxlen)
        return maxlen  
# test 
if __name__ == '__main__':
    # print(Solution().totalFruit([1, 2, 1])) # 3
    print(Solution().totalFruit([0, 0, 3, 3])) # 4
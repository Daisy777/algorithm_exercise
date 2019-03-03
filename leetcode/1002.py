class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import defaultdict
        totald = defaultdict(int)
        for index, word in enumerate(A):
            wordd = defaultdict(int)
            for char in word:
                wordd[char] += 1
            if index == 0:
                totald = wordd

            for key in wordd:
                totald[key] = min(totald[key], wordd[key])
            for key in totald:
                if wordd[key] == 0:
                    totald[key] = 0 
            
        
        result = []
        print(totald)
        for key in totald:
            result.extend([key]*totald[key])
        return result
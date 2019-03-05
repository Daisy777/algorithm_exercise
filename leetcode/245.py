class Solution:
    def shortestWordDistance(self, words: List[int], word1: str, word2: str) -> int:
        # word1 != word2 and word1 and word2 are in words
        # record location 
        from collections import defaultdict
        location = defaultdict(list)
        for index, word in enumerate(words):
            location[word].append(index)
        
        location1 = location[word1]
        location2 = location[word2]
        smallest = float('inf')

        if word1 != word2:
            for l1 in location1:
                for l2 in location2:
                    smallest = min(smallest, abs(l1 - l2))
        else:
            for i in range(len(location1)):
                for j in range(i+1, len(location1)):
                    smallest = min(smallest, location1[j]-location1[i])
        return smallest

# test
if __name__ == '__main__':
    print(Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes")) # 3
        
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # word1 != word2 and word1 and word2 are in words
        # record location 
        from collections import defaultdict
        location = defaultdict(list)
        for index, word in enumerate(words):
            location[word].append(index)
        
        location1 = location[word1]
        location2 = location[word2]
        smallest = float('inf')

        for l1 in location1:
            for l2 in location2:
                smallest = min(smallest, abs(l1 - l2))
        return smallest

# test
if __name__ == '__main__':
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")) # 1
        
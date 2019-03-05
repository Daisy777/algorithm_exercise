class WordDistance:

    def __init__(self, words: List[str]):
        # word1 != word2 and word1 and word2 are in words
        # record location 
        from collections import defaultdict
        self.location = defaultdict(list)
        for index, word in enumerate(words):
            self.location[word].append(index)
            
    def shortest(self, word1: str, word2: str) -> int:
        location1 = self.location[word1]
        location2 = self.location[word2]
        smallest = float('inf')

        for l1 in location1:
            for l2 in location2:
                smallest = min(smallest, abs(l1 - l2))
        return smallest


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
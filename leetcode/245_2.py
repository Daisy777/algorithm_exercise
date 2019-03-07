class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dist = len(words)
        i1 = -1

        for i, word in enumerate(words):
            if word == word1 or word == word2:
                if i1 == -1:
                    i1 = i
                    if word == word2:
                        word1, word2 = word2, word1
                else:
                    if word == word2:
                        min_dist = min(min_dist, i - i1)
                        word1, word2 = word2, word1
                    i1 = i

        return min_dist  
from collections import Counter

class Node:
    def __init__(self, val, child=None):
        self.val = val
        self.child = child

def alien(words):
    # as we use stdin to read in word, it is assumed that len(any word) > 0
    if not words:
        return 0

    # end of words with max frequency
    end = [word[-1] for word in words]

    counter = Counter(end)
    root = Node(counter.most_common(1)[0][0])
    trie = 

    
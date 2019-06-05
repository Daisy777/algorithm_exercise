class Node:
    def __init__(self, value, children, count, terminate):
        self.value = value
        self.children = children 
        self.count = count 
        self.terminate = terminate
    
    def terminate(self):
        self.terminate = True

    def count(self):
        self.count += 1

    def inchild(char):
        for child in self.children:
            if child.value == char:
                return True
        return False

class Trie:
    def __init__(self, root):
        self.root = root
    
    # def find_prefix(self, word):

    def add_word(self, word):
        

'''
Author: ZHAO Zinan
Created: 13. April 2019

428. Serialize and Deserialize N-ary Tree

Serialization is the process of converting a data structure or object into a 
sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. 
An N-ary tree is a rooted tree in which each node has no more than N children. 
There is no restriction on how your serialization/deserialization algorithm
should work. 
You just need to ensure that an N-ary tree can be serialized to a string 
and this string can be deserialized to the original tree structure.
''' 

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return '[]'
        if root.children == []:
            return '[{}]'.format(root.val)
        result = '[{}'.format(root.val)
        for child in root.children:
            result += self.serialize(child)

        return result + ']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data == '[]' or ']':
            return None
        i = 1; j=1
        while(data[j]!='['): j+=1
        root = Node(int(data[i:j]), [])
        i=j

        while(i<len(data)-1 and j<len(data)-1):
            left = 1
            while(left):
                if (data[j]==']'):
                    left -=1
                elif (data[j]=='['):
                    left += 1

            root.children.append(self.deserialize(data[i:j]))
            j+=1; i=j
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
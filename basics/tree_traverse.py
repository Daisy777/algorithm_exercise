# Definition for a binary tree node.
# TODO: add iteration solution

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""preorder recursion"""
def _preoarder(root:TreeNode, result) -> List[int]:
    if root:
        result.append(root.val)
        _preorder(root.left, result)
        _preorder(root.right, result)

def preorderTraversal(root: TreeNode):
    result = []
    _preorder(root, result)
    return result

"""preorder iteration"""
def preorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    
    stack = [root]
    result = []
    while(stack): 
        nodenext = stack.pop()
        result.append(nodenext.val) 
        # s🌟 reminded of in stack, left should be on top of right
        if nodenext.right:
            stack.append(nodenext.right)
        if nodenext.left:
            stack.append(nodenext.left)
        
    return result


"""inorder recursion"""
def _inorder(root:TreeNode, result:List[int]):
    if root:
        _inorder(root.left, result)
        result.append(root.val)
        _inorder(root.right, result)

def inorderTraversal(root: TreeNode) -> List[int]:
        result = []
        _inorder(root, result)
        return result
"""inorder iteration"""
def inorderTraversal(root: TreeNode) -> List[int]:
         # keep to left util we reach the leaf
        result, stack = [], []
        while(True):
            while(root):
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right

"""postorder recursion"""
def _postorder(root:TreeNode, result:List[int]):
    if root:
        _postorder(root.left, result)
        _postorder(root.right, result)
        result.append(root.val)

def postorderTraversal(root: TreeNode) -> List[int]:
        result = []
        _postorder(root, result)
        return result

"""postorder iteration"""
def postorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    
    stack = [root]
    result = []
    while(stack):
        nodenext = stack.pop()
        result.append(nodenext.val)
        if nodenext.left:
            stack.append(nodenext.left)
        if nodenext.right:
            stack.append(nodenext.right)
    result.reverse()
        
    return result
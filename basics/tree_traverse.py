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
    

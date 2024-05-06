# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def BST(s, left, right):
            if not s:
                return True
            if not (s.val < right and s.val > left):
                return False
            return (BST(s.left, left, s.val) and
                    BST(s.right, s.val, right))
                    
        return BST(root, float("-inf"), float("inf"))

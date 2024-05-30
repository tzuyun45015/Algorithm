def check_binary_search_tree_(root):
        def BST(s, left, right):
            if not s:
                return True
            if not (s.data < right and s.data > left):
                return False
            return (BST(s.left, left, s.data) and
                    BST(s.right, s.data, right))
                    
        return BST(root, float("-inf"), float("inf"))

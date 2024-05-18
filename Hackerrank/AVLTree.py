class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self,root,val):
        #step 1 build normal BST
        if not root:
            return TreeNode(val)
        elif root.val < val:
            root.right = self.insert(root.right, val)
        elif root.val > val:
            root.left = self.insert(root.left, val)
        
        #step 2 find unbalanced node from insert node
        root.height = 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        #step 3 find the balanceFactor
        balance = self.getBalance(root)
        
        #step 4 if root not balance rotate (four ways)
        #case 1 left-left
        if balance > 1 and val < root.left.val:
            return self.rightrotate(root)
            
        #case 2 left-right (first left then right)
        if balance > 1 and val > root.left.val:
            root.left = self.leftrotate(root.left)
            return self.rightrotae(root)
            
        #case 3 right-right
        if balance < -1 and val > root.right.val:
            return self.leftrotate(root)
            
        #case 4 right-left (first right then left)
        if balance < -1 and val < root.right.val:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)
        
        return root
            
    def maxDepth(self, root):
            if not root:
                return 0
            return root.height
    
    def getBalance(self,root):
        if not root:
            return 0
        return self.maxDepth(root.left) - self.maxDepth(root.right)
    
    def rightrotate(self,root):
        y = root.left
        x = y.right
        
        y.right = root
        root.left = x
        
        root.height = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        y.height = 1 + max(self.maxDepth(y.left), self.maxDepth(y.right))
        return y #return the new root
        
    def leftrotate(self,root):
        y = root.right
        x = y.left
        
        y.left = root
        root.right = x
        
        root.height = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        y.height = 1 + max(self.maxDepth(y.left), self.maxDepth(y.right))
        return y #return the new root
    
    def preOrder(self, root): 
        if not root:
            return
        print(f"{root.val}(BF={self.getBalance(root)})", end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    def inOrder(self, root): 
        if not root: 
            return
        self.inOrder(root.left) 
        print(f"{root.val}(BF={self.getBalance(root)})", end=" ")
        self.inOrder(root.right)
        

if __name__ == "__main__":        
    myTree = AVLTree() 
    t = int(input())
    arr = list(map(int, input().split()))
    root = None

    for i in arr:
        root = myTree.insert(root,i)
    root = myTree.insert(root, int(input()))
    #print
    
    myTree.inOrder(root)
    print()
    myTree.preOrder(root)

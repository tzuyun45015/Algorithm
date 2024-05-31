class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(indexes):
    if not indexes:
        return None
    root = Node(1)
    q = deque([root])
    for left, right in indexes:
        cur = q.popleft()
        if left != -1:
            cur.left = Node(left)
            q.append(cur.left)
        if right != -1:
            cur.right = Node(right)
            q.append(cur.right)
    return root

def swapTree(root,k):
    if not root:
        return []
    q = deque([(1,root)])
    while q:
        level,node = q.popleft()
        if level % k == 0:
            temp = node.left
            node.left = node.right
            node.right = temp 
        if node.left:
            q.append((level+1, node.left))
        if node.right:
            q.append((level+1, node.right))
                
    return root
    
def inorder(root,tree):
    q = deque()
    curr=root
    while True:
        if curr!=None and curr.val!=-1:
            q.append(curr)
            curr=curr.left
        elif q:
            curr=q.pop()
            tree.append(curr.val)
            curr=curr.right
        else:
            break
    return tree
    

def swapNodes(indexes, queries):
    # Write your code here
    result=[]
    root=buildTree(indexes)
    for level in queries:
        root=swapTree(root,level)
        tree=[]
        tree=inorder(root,tree)
        result.append(tree)
    return result

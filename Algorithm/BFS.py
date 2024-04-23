#breadth first search
#queue: first in first out
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #breadth first search
        #queue: first in first out
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

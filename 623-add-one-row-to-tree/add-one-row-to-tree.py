# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:

            node = TreeNode(val)
            node.left = root

            return node

        que = deque([root])
        d = 1

        while que:

            d += 1

            for _ in range(len(que)):
                
                node = que.popleft()

                if d == depth:

                    left = TreeNode(val)
                    right = TreeNode(val)

                    left.left, right.right = node.left, node.right

                    node.left, node.right = left, right
                
                if node.left:
                    que.append(node.left)
                    
                if node.right:
                    que.append(node.right)
                    
            if d == depth:
                break

        return root
                












       

            
        


        
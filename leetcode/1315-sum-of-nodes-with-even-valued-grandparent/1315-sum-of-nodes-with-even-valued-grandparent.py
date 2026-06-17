class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if root and (not root.left and not root.right): return 0
        q= deque()
        q.append([root, None, None])
        # m
        ans=0
        while q:
            r, p, gr= q.popleft()
            if gr and gr.val%2==0: ans+=r.val
            if r.left: q.append([r.left, r, p])
            if r.right: q.append([r.right, r, p])
        return ans
            
                

                                    
            
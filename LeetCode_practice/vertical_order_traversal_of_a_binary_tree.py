# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level_items = defaultdict(list)
        queue = deque([(0, 0, root)])

        max_col = float('-inf')
        min_col = float('inf')

        while queue:
            r, c, node = queue.popleft()
            max_col = max(max_col, c)
            min_col = min(min_col, c)

            level_items[c].append((node.val, r))

            if node.left:
                queue.append((r + 1, c - 1, node.left))
            if node.right:
                queue.append((r+1, c+1, node.right))
            
        res = []

        for level in range(min_col, max_col+1):
            items = level_items[level]
            items.sort(key=lambda x: (x[1], x[0]))
            items = [val for val, _ in items]
            res.append(items)
        
        return res

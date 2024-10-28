# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        col_items = defaultdict(list)
        queue = deque([(0, root)])

        min_level = float('inf')
        max_level = float('-inf')

        res = []

        while queue:
            level, node = queue.popleft()
            col_items[level].append(node.val)
            min_level = min(min_level, level)
            max_level = max(max_level, level)

            if node.left:
                queue.append((level - 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        
        for level in range(min_level, max_level + 1):
            res.append(col_items[level])
        
        return res
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def get_total(node):
            if not node: return 0 
            l = get_total(node.left)
            r = get_total(node.right)
            return l + r + node.val
        
        def test_edges(node):
            if not node: return 0 
            l = test_edges(node.left)
            r = test_edges(node.right)
            self.res = max(self.res, l * (total-l), r*(total -r))
            return l + r + node.val
        
        self.res = 0
        total = get_total(root)
        test_edges(root)
        return self.res%MOD
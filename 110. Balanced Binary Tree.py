# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         return (self.Height(root) >= 0)
#     def Height(self, root: Optional[TreeNode]) -> bool:
#         if root is None:  return 0
#         leftheight, rightheight = self.Height(root.left), self.Height(root.right)
#         if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
#         return max(leftheight, rightheight) + 1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
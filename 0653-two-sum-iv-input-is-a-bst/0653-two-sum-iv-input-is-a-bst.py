# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k):
        # Step 1: Inorder traversal to get sorted values
        def inorder(node, arr):
            if not node:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
        
        nums = []
        inorder(root, nums)
        
        # Step 2: Two-pointer approach
        left, right = 0, len(nums) - 1
        
        while left < right:
            curr_sum = nums[left] + nums[right]
            
            if curr_sum == k:
                return True
            elif curr_sum < k:
                left += 1
            else:
                right -= 1

        return False
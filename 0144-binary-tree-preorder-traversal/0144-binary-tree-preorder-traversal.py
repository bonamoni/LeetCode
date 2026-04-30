class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root

        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    res.append(curr.val)   # preorder position
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    curr = curr.right

        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):

            if not t1 and not t2:
                return True

            if not t1 or not t2 or t1.val != t2.val:
                return False

            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root, root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

test = Solution()
print(test.isSymmetric(root))
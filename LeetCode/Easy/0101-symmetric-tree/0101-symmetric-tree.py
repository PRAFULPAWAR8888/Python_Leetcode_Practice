# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(t1,t2):
            

            # casse 1: both are None
            if not t1 and not t2:
                return True
            

            # one is none
            if not t1 or not t2:
                return False
            
            # values are differnt
     
            if t1.val != t2.val:
                return False

            # Mirror Comparison
            return (isMirror(t1.left,t2.right) and isMirror(t1.right,t2.left))
        return isMirror(root.left, root.right)

                       
        
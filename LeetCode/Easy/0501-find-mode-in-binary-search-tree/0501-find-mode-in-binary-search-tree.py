# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if(root.left == None and root.right == None):
            return [root.val]
        
        def check_duplicates(root):
            if (root.val not in count):
                count[root.val] = 1
            
            else:
                count[root.val] += 1
            
            if (root.left != None):
                check_duplicates(root.left)
            
            if (root.right != None):
                check_duplicates(root.right)
        
        count = {}

        check_duplicates(root)
        result = []
        maxi = max(count.values())
        for key, val in count.items():
            if (val == maxi):
                result.append(key)
        return result
        
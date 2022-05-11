# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root):
        count = 0
        if root:
            if root.left is not None:
                if root.right is None:
                    count += 1
                
                count += self.solve(root.left)
            
            if root.right is not None:
                if root.left is None:
                    count += 1
                
                count += self.solve(root.right)
        return count

        
       0
    4.   2
       1
     3
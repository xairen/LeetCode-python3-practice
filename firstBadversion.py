# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n<2:
            return n
        
        left = 1
        right = n
        while left<right:
            check=left+(right-left)//2
            if isBadVersion(check):
                right = check
            else:
                left = check + 1
        return left
    
    
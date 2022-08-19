# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        
        while (left < right):
            middle = (left + right) // 2
            if (isBadVersion(middle)):
                right = middle
            else:
                left = middle + 1
                
        if ( left == right and isBadVersion(left) ):
            return left
                
        return -1
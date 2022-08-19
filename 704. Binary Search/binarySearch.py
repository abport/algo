# Complexity ----------------------------------------------------------
# Time: O(log(n)) | Space: O(1) 
# ---------------------------------------------------------------------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        
        while (left<= right):
            middle = (left + right) // 2
            potentialMatch = nums[middle]
            
            if target == potentialMatch:
                return middle
            elif target < potentialMatch:
                right = middle - 1
            else:
                left = middle + 1
        return -1
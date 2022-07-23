# Two Number Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numsSorted = nums[:]
        numsSorted.sort()

        left = 0
        right = len(nums) - 1
        
        while left < right :
            
            currentSum = numsSorted[left] + numsSorted[right]
            if currentSum == target:
                a = numsSorted[left]
                b = numsSorted[right]
                if a == b:
                    tempIndex = []
                    for i in range(len(nums)):
                        if nums[i] == a:
                            tempIndex.append(i)
                            i += 1
                    return tempIndex
                return [nums.index(a),nums.index(b)]
            elif currentSum < target :
                left += 1
            elif currentSum > target :
                right -= 1
        return []

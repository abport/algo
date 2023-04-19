class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sorted_nums = sorted(nums)

        left = 0
        right = len(nums) - 1

        while left < right:

            current_sum = sorted_nums[left] + sorted_nums[right]

            if current_sum == target:
                a = sorted_nums[left]
                b = sorted_nums[right]

                if a == b:
                    a_index = nums.index(a)
                    b_index = nums.index(b, a_index + 1)
                    return [a_index, b_index]

                return [nums.index(a), nums.index(b)]

            elif current_sum < target:
                left += 1

            elif current_sum > target:
                right -= 1

        return []

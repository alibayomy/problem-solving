"""53. Maximum Subarray"""
"""

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""
from typing import List


class Solution:
    def maxSubArrayNaive(self, nums: List[int]) -> int:
        largest_sum = nums[0]
        for start in range(len(nums)):
            current_sum = 0
            for end in range(start, len(nums)):
                current_sum += nums[end]
                largest_sum = max(current_sum, largest_sum)
            
        return largest_sum

    def maxSubArrayOpt(self, nums:List[int]) -> int:
        largest_sum = nums[0]
        index = 0
        current_sum = 0
        while index < len(nums):
            current_sum += nums[index]
            current_sum = max(current_sum, 0)
            largest_sum = max(current_sum, largest_sum)
            index += 1
        return largest_sum
            
sol = Solution()
print(sol.maxSubArrayNaive([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArrayOpt([-2,1,-3,4,-1,2,1,-5,4]))


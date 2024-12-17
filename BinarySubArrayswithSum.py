class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atmost(nums, goal):
            if goal < 0 : return 0
            left = right = 0
            s = ctr = 0
            while right < len(nums):
                s += nums[right]
                while s > goal:
                    s -= nums[left]
                    left += 1
                ctr = ctr + (right - left + 1)
                right += 1
            return ctr
        return atmost(nums, goal) - atmost(nums, goal-1)
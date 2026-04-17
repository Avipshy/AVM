class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        
        max_len = 0
        for num in nums:
            if (num - 1) not in nums:
                cur = num
                while (cur + 1) in nums:
                    cur += 1
                max_len = max(max_len, cur - num + 1)

        return max_len
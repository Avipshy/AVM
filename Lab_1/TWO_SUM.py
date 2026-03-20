class Solution:
    def TwoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            seen[num] = idx

sol = Solution()

print(f'nums = [2,7,11,15], target = 9: {sol.TwoSum([2,7,11,15], 9)}')
print(f'nums = [3,2,4], target = 6: {sol.TwoSum([3,2,4], 6)}')
print(f'nums = [3,3], target = 6: {sol.TwoSum([3,3], 6)}')
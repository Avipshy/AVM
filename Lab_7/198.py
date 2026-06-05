class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            cur_max = max(rob2, rob1 + n)

            rob1 = rob2
            rob2 = cur_max
        
        return rob2
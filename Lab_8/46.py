class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        used = [False] * len(nums)

        def backtrack():
            if len(cur) == len(nums):
                res.append(list(cur))
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    cur.append(nums[i])
                    backtrack()
                    cur.pop()
                    used[i] = False
        backtrack()
        return res
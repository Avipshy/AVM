class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(start, cur_sum):
            if cur_sum == target:
                res.append(list(cur))
                return
            if cur_sum > target:
                return
            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                backtrack(i, cur_sum + candidates[i])
                cur.pop()
        backtrack(0, 0)
        return res
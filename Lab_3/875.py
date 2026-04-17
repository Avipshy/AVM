import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = right

        while left <= right:
            k = left + (right - left) // 2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / k)
        
            if total_hours <= h:
                min_k = k
                right = k - 1
        
            else:
                left = k + 1

        return min_k
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_map = {}
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        
        sorted_keys = sorted(count_map, key=count_map.get, reverse=True)

        return sorted_keys[:k]
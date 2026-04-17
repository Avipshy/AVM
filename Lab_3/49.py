class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_table = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)

            if key not in hash_table:
                hash_table[key] = []
            
            hash_table[key].append(s)
        
        return list(hash_table.values())
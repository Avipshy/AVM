class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        left = 0
        known = set()
        for right, char in enumerate(s):
            while char in known:
                known.remove(s[left])
                left += 1
            known.add(char)
            maxlen = max(maxlen, right - left + 1)
        return maxlen
    

sol = Solution()

print(f'"abcabcbb" : {sol.lengthOfLongestSubstring("abcabcbb")}')
print(f'"bbbbb" : {sol.lengthOfLongestSubstring("bbbbb")}')
print(f'"pwwkew" : {sol.lengthOfLongestSubstring("pwwkew")}')
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_container = 0
        while left < right:
            container = (right - left) * min(height[left], height[right])
            max_container = max(max_container, container)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_container
sol = Solution()

print(f'height = [1,8,6,2,5,4,8,3,7] : {sol.maxArea([1,8,6,2,5,4,8,3,7])}')
print(f'height = [1,1] : {sol.maxArea([1,1])}')
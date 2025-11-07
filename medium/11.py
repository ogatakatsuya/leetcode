class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height) - 1
        results = []
        while start < end:
            if height[start] < height[end]:
                results.append((end-start)*height[start])
                start += 1
            else:
                results.append((end-start)*height[end])
                end -= 1
        return max(results)

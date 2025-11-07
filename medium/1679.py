from collections import Counter

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        c = Counter(nums)
        half_count = 0
        count = 0
        for key, value in c.items():
            if key == k/2:
                half_count = int(value/2)
                continue
            count += min(value, c[k-key])
        return int(count/2) + half_count

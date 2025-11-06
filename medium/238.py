""" TimeOut
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        results = []
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            results.append(product)
            product = 1
        return results
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        results = [1] * n
        left = 1
        for i in range(n):
            results[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            results[i] *= right
            right *= nums[i]
        return results

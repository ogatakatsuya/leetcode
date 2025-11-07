class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1

        left, right = 0, sum(nums)

        for i in range(len(nums)):
            left += nums[i - 1] if i > 0 else 0
            right -= nums[i]

            if left == right:
                return i

        return -1

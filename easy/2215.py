class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # ans1 = []
        # ans2 = []

        # for i in nums1:
        #     if i not in nums2 and i not in ans1:
        #         ans1.append(i)

        # for j in nums2:
        #     if j not in nums1 and j not in ans2:
        #         ans2.append(j)

        # return [ans1, ans2]

        set1, set2 = set(nums1), set(nums2)

        list1 = [num for num in set1 if num not in set2]
        list2 = [num for num in set2 if num not in set1]

        return [list1, list2]

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        c = Counter(arr)

        count_list = c.values()
        count_set = set(c.values())

        return len(count_list) == len(list(count_set))

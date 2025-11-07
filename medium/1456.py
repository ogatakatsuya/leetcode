class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0
        for i in range(k):
            if vowels.find(s[i]) != -1:
                count += 1
        max_count = count

        for i in range(k, len(s)):
            count -= 1 if vowels.find(s[i-k]) != -1 else 0
            count += 1 if vowels.find(s[i]) != -1 else 0
            max_count = max(max_count, count)

        return max_count
    
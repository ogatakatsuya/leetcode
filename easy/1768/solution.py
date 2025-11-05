class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)

        max_length = word1_len if word1_len >= word2_len else word2_len

        result = ""
        for idx in range(max_length):
            result += word1[idx] if idx+1 <= word1_len else "" 
            result += word2[idx] if idx+1 <= word2_len else ""

        return result
    
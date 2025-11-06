class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = []
        for i in range(1,len(s)+1):
            result.append(s[-i])
        return (" ").join(result)

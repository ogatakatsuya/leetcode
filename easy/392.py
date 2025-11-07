class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        read = 0
        for char in s:
            if read >= len(t):
                return False
            while char != t[read]:
                read += 1
                if read >= len(t):
                    return False
            read += 1
        return True
    
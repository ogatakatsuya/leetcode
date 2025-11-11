class Solution:
    def removeStars(self, s: str) -> str:
        # result = []
        # s = list(s)

        # while len(s) > 0:
        #     char = s.pop(0)
        #     if char == '*':
        #         if len(result) > 0:
        #             result.pop(-1)
        #     else:
        #         result.append(char)
        # return ('').join(result)
        result = []

        for c in s:
            if c == "*":
                if result:
                    result.pop(-1)
            else:
                result.append(c)
        return "".join(result)

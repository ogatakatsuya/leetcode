"""
class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1
        results = [chars[0]]
        for i in range(1, len(chars)):
            if chars[i-1] == chars[i]:
                count += 1
            else:
                if count > 1:
                    for c in str(count):
                        results.append(c)
                count = 1
                results.append(chars[i])
        if count > 1:
            for c in str(count):
                results.append(c)
        return results
"""
    
class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1
        write = 0
        for i in range(1, len(chars)+1):
            if i < len(chars) and chars[i-1] == chars[i]:
                count += 1
            else:
                chars[write] = chars[i-1]
                write += 1
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1
                count = 1
        return write


if __name__ == "__main__":
    solution = Solution()
    print(solution.compress(["a", "a", "b", "b", "c", "c", "c"]))
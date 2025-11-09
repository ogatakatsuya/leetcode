class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                char = stack.pop()
                target = ""
                while char != "[":
                    target = char + target
                    char = stack.pop()
                num = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    num = stack.pop() + num
                for _ in range(int(num)):
                    for c in target:
                        stack.append(c)
        return "".join(stack)

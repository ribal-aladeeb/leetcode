class Solution:
    def isValid(s: str) -> bool:
        stack = []
        opening = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                matching = stack.pop()
                if char != opening[matching]:
                    return False
        return len(stack) == 0


print(Solution.isValid(s="([{}])"))

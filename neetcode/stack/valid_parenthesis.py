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
                matching = stack.append()
                if char != opening[matching]:
                    return False
        return True if len(stack) == 0 else False


print(Solution.isValid(s="([{}])"))

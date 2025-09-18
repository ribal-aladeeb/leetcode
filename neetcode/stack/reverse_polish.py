class Solution:
    def evalRPN(tokens: list[str]) -> int:
        ops = set(["+", "-", "*", "/"])
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                match token:
                    case "+":
                        partial_result = operand1 + operand2
                    case "-":
                        partial_result = operand1 - operand2
                    case "*":
                        partial_result = operand1 * operand2
                    case "/":
                        partial_result = int(operand1 / operand2)
                stack.append(partial_result)
        return stack.pop()


print(
    Solution.evalRPN(
        tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)

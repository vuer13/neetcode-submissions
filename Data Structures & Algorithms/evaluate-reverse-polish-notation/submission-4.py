class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for t in tokens:
            if t in operations:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if t == "+":
                    num = num1 + num2
                elif t == "-":
                    num = num2 - num1
                elif t == "*":
                    num = num1 * num2
                else:
                    num = num2 / num1
                stack.append(num)
            else:
                stack.append(t)
            print(stack)

        return stack.pop()

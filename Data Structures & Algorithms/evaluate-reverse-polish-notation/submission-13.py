class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operations:
                int1 = int(stack.pop())
                int2 = int(stack.pop())
                if token == "+":
                    new_num = int1 + int2
                elif token == "-":
                    new_num = int2 - int1
                elif token == "*":
                    new_num = int1 * int2
                else:
                    new_num = int(int2 / int1)
                stack.append(new_num)
            else:
                stack.append(int(token))

        return int(stack.pop())


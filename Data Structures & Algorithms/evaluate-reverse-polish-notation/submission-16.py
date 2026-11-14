class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # We want to calculate the value of an expression given the version in "polish" notation
        
        # Assumptions:
        # 1. tokens is a valid list such that
        # a. each operation can be ran without any issues (ie. there are 2 numbers before it)
        # b. operations are +, -, *, /
        # c. we cannot do illegal operations (ie. divide by 0)
        # 2. When we divide, we take the floor of the value
        # 3. BEDMAS doesn't apply, just the order of the "tokens"
        # 4. We either end the list of tokens with an operation, or just unused numbers

        # [] => None; I don't want to return 0 since an undefined expression should remain undefined
        # [1] => 1; We do nothing with 1, so might as well return 1
        # [1, 2] => None; Invalid operation
        # [1, 2, +] => 3
        # [1, 2, -, +] => Invalid
        # [1, 2, +, 3, -] => 0

        # We quickly see, it's invalid if there are not two numbers remaining that we can perform an operation with
        # It is also invalid if at the end of everything, we have 2 numbers to do "something" with

        # We need something to store the previous numbers to use
        # I think a "stack" would be a good idea
        # We can store numbers, perform operations and store the result back there
        # So what we can do is go through tokens
        # If it is a number, add to the stack
        # If not a number, perform the operation, add back to the stack
        # If we cannot perform the operation, return None
        # If at the end more than one number exists, return None

        stack = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operations:
                if len(stack) >= 2:
                    first_elem = stack.pop()
                    second_elem = stack.pop()
                else:
                    return None

                if token == operations[0]:
                    num = first_elem + second_elem
                elif token == operations[1]:
                    num = second_elem - first_elem
                elif token == operations[2]:
                    num = first_elem * second_elem
                else:
                    num = int(second_elem / first_elem)

                stack.append(num)
            else:
                stack.append(int(token))

        num = stack.pop()
        return num if len(stack) == 0 else None

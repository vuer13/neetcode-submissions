class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for p in s:
            if stack and stack[-1] == pairs.get(p):
                stack.pop()
            else:
                stack.append(p)
            print(stack)
        
        return len(stack) == 0
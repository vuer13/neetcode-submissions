class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []

        for string in s:
            if string == '(':
                left.append(string)
            elif string == '*':
                stars.append(string)
            else:
                if not left and not stars:
                    return False
                if left:
                    left.pop()
                else:
                    stars.pop()
        
        return len(left) <= len(stars)
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
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else: 
                    return False
        
        return len(left) <= len(stars)
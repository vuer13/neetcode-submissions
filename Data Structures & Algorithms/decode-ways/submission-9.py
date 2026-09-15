class Solution:
    def numDecodings(self, s: str) -> int:
        possible_combinations = {len(s) : 1}

        def numDecodingsHelper(i):
            if i in possible_combinations:
                return possible_combinations[i]
            if s[i] == '0':
                return 0

            result = 0
            result += numDecodingsHelper(i + 1)

            if (
                i + 1 < len(s) and
                (s[i] == "1" or 
                (s[i] == "2" and s[i + 1] in "0123456"))
            ):
                result += numDecodingsHelper(i + 2)

            possible_combinations[i] = result
            return result

        return numDecodingsHelper(0)

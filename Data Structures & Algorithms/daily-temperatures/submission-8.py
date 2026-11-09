class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We want an array that represents the number of days until the next 
        # hottest temperature
        # We need someway to store the next "hottest" date compared to the previous date

        # Assumptions:
        # 1. Temperatures has at least 1 element
        # 2. Temperatures in temperatures are any number

        # [] => []
        # [1] => [0]
        # [1, 2] => [1, 0]
        # [1, 0] => [0, 0]
        # [1, 1] => [0, 0]
        # [1, 1, 1] => [0, 0, 0]
        # [2, 1, 0] => [0, 0, 0]
        # [2, 1, 1] => [0, 0, 0]
        # [1, 2, 3] => [1, 1, 0]
        # [1, 2, 1] => [1, 0, 0]
        # [2, 1, 3] => [2, 0, 0]
        # What I've noticed:
        # We need to track the index of the date essentially
        # When we encounter a date, we need to store it somewhere to see, is there 
        # a hotter day

        # We can use a queue or stack to store the previous state
        # We need to compare all previous days to the current day
        # Stack would be best with the first in, last out 
        # We need to check the last date to see if its colder than the current date
        # If it isn't, then we can keep it to the stack and add the new date
        # This works b/c anything in the stack below has to be hotter
        # Otherwise, we could've popped it long ago

        # We also must keep track on the date somewhere, so we know when to update

        n = len(temperatures)

        result = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, last_date = stack.pop()
                result[last_date] = i - last_date
            stack.append((temp, i))

        return result

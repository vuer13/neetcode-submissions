class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(p, s) for p, s in zip(position, speed)]
        pos_speed.sort(reverse=True)

        stack = []

        for p, s in pos_speed:
            time = (target - p) / s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
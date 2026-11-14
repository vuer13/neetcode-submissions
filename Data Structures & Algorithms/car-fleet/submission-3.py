class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We need to find number of groups that cross the finish line
        # A car joins a group if it is going to PASS a car ahead of it
        # - it isn't actually allowed to, but if is going to eventually (before the target)
        # - then that's a group
        
        # Assumptions:
        # Both speed and position are valid arrays such that speed is > 0 and position is >= 0
        # target is also >= 0
        # all values in position are less than target (or equal to I guess)
        # Speed and position have the same length

        # Positions, Speed, Target
        # [], [], 0 => 0
        # [1], [1], 10 => 1
        # [1, 1], [1, 1], 5 => 1 group, moves together 
        # [1, 2], [1, 1], 5 => 2 groups
        # [1, 2], [2, 1], 5 => 1 group
        # [1, 2], [1, 2], 5 => 2 groups 
        # [2, 1], [1, 1], 5 => 2 groups
        # [2, 1], [1, 2], 5 => 1 group
        # [2, 1], [2, 1], 5 => 2 groups
        # Observations so far:
        # I mentioned a lot about cars behind "catching up" eventually
        # So essentially, I think we need to check, does this car behind me catch up eventually
        # If so, keep checking until a car doesn't catch up
        # That is one group
        # We repeat for anything else behind
        # What does catch up mean, well it needs to PASS the car (or meet it)
        # We can measure that with time it takes to get to the end
        # For this group, if the time is >= the car ahead, it joins that group

        # Implementation:
        # Sort by position first
        # For each position, if this time to reach target is >= the leader of the group, then add it to the group
        # NOTE: we need to know group leader
        # - we know that what will limit us (which is likely the furthest car, since we cannot pass it)
        # We need some way of keeping it
        # We can use an array to all group leaders and return the length of that

        group_leaders = []
        pos_speed = [(p, s) for p, s in zip(position, speed)]
        pos_speed.sort(reverse=True)

        for p, s in pos_speed:
            time = (target - p) / s
            if group_leaders and group_leaders[-1] >= time:
                continue
            group_leaders.append(time)
        
        return len(group_leaders)

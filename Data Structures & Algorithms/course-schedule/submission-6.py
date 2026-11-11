class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We want to see, is it possible to finish all courses
        # We have pre-reqs for each course
        # We likely need some sort of "ordering" algorithm to order everything

        # Topological sort
        # [a, b] where both a and b are valid "numbers"
        # numCourses is >= 0
        # No pre-reqs means there could be a bunch of courses you can still take
        # that may not have a pre-req
        # In that case, we could return True?
        # Situational, depends i guess

        # We need a topological sort or DFS
        # 1. Starting at ALL non pre-req courses
        # 2. From there, go to all it's next "courses"
        # 3. When we get there, minus one from its in-degree
        # 4. Afterwards, if it's indegree is 0 (ie. all pre-reqs are completed)
        # add to the queue

        adj_list = defaultdict(list)
        in_degrees = [0] * (numCourses)
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degrees[course] += 1

        queue = deque()
        for i, degree in enumerate(in_degrees):
            if degree == 0:
                queue.append(i)
        taken = 0
        while queue:
            curr_course = queue.popleft()
            taken += 1
            for next_course in adj_list[curr_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        return taken == numCourses

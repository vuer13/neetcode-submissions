class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological sort is needed here
        adj_list = defaultdict(list)
        in_degrees = [0] * numCourses

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degrees[course] += 1
        
        queue = deque()
        for i, degree in enumerate(in_degrees):
            if degree == 0:
                queue.append(i)

        course = 0
        while queue:
            c = queue.popleft()
            course += 1

            for next_course in adj_list[c]:
                in_degrees[next_course] -= 1

                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        return course == numCourses

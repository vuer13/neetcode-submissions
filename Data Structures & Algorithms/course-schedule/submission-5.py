class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_matrix = defaultdict(list)
        in_degrees = [0] * numCourses
        for course, pre in prerequisites:
            adj_matrix[pre].append(course)
            in_degrees[course] += 1

        queue = deque()
        for i, degree in enumerate(in_degrees):
            if degree == 0:
                queue.append(i)

        course = 0
        while queue:
            node = queue.popleft()
            course += 1

            for neighbour in adj_matrix[node]:
                in_degrees[neighbour] -= 1
                if in_degrees[neighbour] == 0:
                    queue.append(neighbour)

        return course == numCourses
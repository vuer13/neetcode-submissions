class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Directed graph
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        for post, pre in prerequisites:
            adj_list[pre].append(post)
            indegree[post] += 1

        queue = deque()
        for i, degree in enumerate(indegree):
            if degree == 0:
                queue.append(i)

        courses = []
        while queue:
            node = queue.popleft()
            courses.append(node)

            for neighbour in adj_list[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return courses if len(courses) == numCourses else []
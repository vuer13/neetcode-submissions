class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        courses_taken = 0
        while queue:
            node = queue.popleft()
            courses_taken += 1

            for neighbour in adj_list[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return courses_taken == numCourses

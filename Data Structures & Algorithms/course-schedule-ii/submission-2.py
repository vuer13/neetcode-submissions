class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Given a directed graph (essentially), give the order
        # Topological sort

        adj_list = defaultdict(list)
        in_degrees = [0] * numCourses
        for course, pre_req in prerequisites:
            adj_list[pre_req].append(course)
            in_degrees[course] += 1

        queue = deque()
        # Append all courses with no pre reqs
        for course, degree in enumerate(in_degrees):
            if degree == 0:
                queue.append(course)

        order = []
        while queue:
            current_course = queue.popleft()
            order.append(current_course)

            for next_course in adj_list[current_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == numCourses else []

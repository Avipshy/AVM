class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_req = {}

        for course, pre in prerequisites:
            if course not in course_req:
                course_req[course] = []
            course_req[course].append(pre)
        
        path = set()

        def dfs(course):
            if not course_req.get(course):
                return False

            if course in path:
                return True
            
            path.add(course)

            for prereq in course_req[course]:
                if dfs(prereq):
                    return True
            
            path.remove(course)

            course_req[course] = []
            return False
        
        for course in range(numCourses):
            if dfs(course):
                return False
        return True
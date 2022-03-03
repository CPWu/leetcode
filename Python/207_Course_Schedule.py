# 1 Possible Solutions
# 1. Sort Items

class Solution:
    # DFS
    # Time: O(V+E), Space: O(V+E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adj list
        prereqMap = {i: [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
            
        visited = set()
        
        for course in range(numCourses):
            if not self.dfs(course, prereqMap, visited): 
                return False
        return True
    
    def dfs(self,course, prereqMap, visited):
        if course in visited:
            return False
        # Course has no prereq
        if prereqMap[course] == []:
            return True
        
        visited.add(course)
        
        for prereq in prereqMap[course]:
            if not self.dfs(prereq, prereqMap, visited):
                return False
        visited.remove(course)
        prereqMap[course] = []     
        return True
# 1 Possible Solutions
# 1. DFS


class Solution:
    # DFS
    # Time: O(E+V), Space: O(E+V)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Empty Tree is still a valid Tree
        if not n:
            return True
        
        adjacencyList = {i:[] for i in range(n)}
        visited = set()
        
        for n1, n2 in edges:
            adjacencyList[n1].append(n2)
            adjacencyList[n2].append(n1)
        
        return self.traverseGraph(0, -1, visited, adjacencyList) and n == len(visited)

    def traverseGraph(self, node, prev, visited, adjacencyList):
        if node in visited:
            return False
        
        visited.add(node)
        
        for neighbour in adjacencyList[node]: 
            if neighbour == prev:
                continue
            if not self.traverseGraph(neighbour, node, visited, adjacencyList):
                return False
        return True
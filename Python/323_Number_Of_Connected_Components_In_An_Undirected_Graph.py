# 4 Possible Solutions
# 1. DFS
# 2. BFS
# 3. Union Find with Union by Rank

class Solution:
    # DFS
    # Time: O(E+V), Space: O(E+V)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        componentCount = 0
        visited = set()
        
        # Since its undirected the path can be both ways
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        for node in range(n):
            if node not in visited:
                self.traverseComponent(node, visited, graph)
                componentCount += 1
        return componentCount

    def traverseComponent(self, node: int, visited: set, graph: dict) -> int:
        # Add node to set so we do not visit again
        visited.add(node)
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                self.traverseComponent(neighbour, visited, graph)

    # BFS
    # Time: O(E+V), Space: O(E+V)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        componentCount = 0
        visited = set()
        
        # Since its undirected the path can be both ways
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                self.traverseComponent(node, visited, graph)
                componentCount += 1
        return componentCount

    def traverseComponent(self, node: int, visited: set, graph: dict) -> int:
        queue = collections.deque([node])
        
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                
    # Union Find
    # Time: O(E+V), Space: O(V)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # parentArray for each node
        parentArray = list(range(n))
        # Rank
        rank = [1] * n
        
                           
        # Given a node find its root parent
        def find(node):
            result = node
            
            while result != parentArray[result]:
                parentArray[result] = parentArray[parentArray[result]]
                result = parentArray[result]
            
            return result
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parent1 == parent2:
                return 0
            
            if rank[parent2] > rank[parent1]:
                parentArray[p1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parentArray[parent2] = parent1
                rank[parent2] += rank[parent2]
            return 1
        
        result = n
        for node1, node2 in edges:
            result -= union(node1, node2)
        return result

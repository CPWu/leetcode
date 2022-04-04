# Introduction to Graphs #

# Single List Comprehension

# [A]-----[B]
# |       |
# |       |
# |       |
# [C]-----[D]-----[E]

# Let V represent your vertexs or nodes
# Let E represent the edge.

# V = {a, b, c, d, e}
# E = {ab, ac, bd, cd, de}

# Create a dictionary to represent the graph elements
graph = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"],
}

print(graph)

# Display Graph Vertices
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Old School Way
myList = []
for num in nums:
    myList.append(num)
print(nums)

# List Comprehension
myList = [num for num in nums]
# List Comprehension with Expression
myList = [num*num for num in nums]
# Using a Map & Lambda (Anonymous Function)
myList = map(lambda num: num * num, nums)
# Generating 2-Day Array
twoDimensionalArray = [[0 for col in range(columns) for row in range(rows)]]

import heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!

heapq.heappop(minheap)      # pop from minheap
heapq._heappop_max(maxheap) # pop from maxheap

# 1 Possible Solutions
# 1. BFS Graphing

class Solution:
    # Time: (M^2*N), Space: (M^2*N)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # end word doesn't exist in word list
        if endWord not in wordList:
            return 0
        
        adjList = collections.defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adjList[pattern].append(word)
                
        visited = set([beginWord])
        queue = collections.deque([beginWord])    
        result = 1
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbourWord in adjList[pattern]:
                        if neighbourWord not in visited:
                            visited.add(neighbourWord)
                            queue.append(neighbourWord)              
            result += 1
        return 0
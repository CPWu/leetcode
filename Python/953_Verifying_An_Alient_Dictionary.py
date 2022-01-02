class Solution(object):
    # Time: O(N+M) N - orderIndex, M - inputSize, Space: O(1)
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderIndex = { c : i for i, c in enumerate(order) }
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if orderIndex[words[i][j]] > orderIndex[words[i+1][j]]:
                        return False
                    break
        return True

soln = Solution()
words = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
order = "zkgwaverfimqxbnctdplsjyohu"

print(soln.isAlienSorted(words, order))

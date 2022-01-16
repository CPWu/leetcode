class Solution:
    # Time: O(N), Space: O(N)
    def customSortString(self, order: str, s: str) -> str:
        lookup = defaultdict(int)
        i = 0

        for character in order:
            lookup[character] = i
            i += 1

        return "".join(sorted(s,key=lambda x:lookup[x]))
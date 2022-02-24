# 2 Possible Solutions
# 1. Dictionary to Index Order
# 2. Counting Sort/Dictionary

    # Time: O(NLogN), Space: O(1)
    def customSortString(self, order: str, s: str) -> str:
        lookup = defaultdict(int)
        i = 0

        # Create lookup based on int order of order string.
        for character in order:
            lookup[character] = i
            i += 1

        # Sort String
        return "".join(sorted(s,key=lambda x:lookup.get(x, 100))


    # Time: O(N), Space: O(1)
    def customSortString(self, order: str, s: str) -> str:
        # Use collections.Count to count frequency of characters in S
        count = collections.Counter(s)
        result = []
        
        # Write all characters that occur in S, in the order of S
        for character in order:
            result.append(character * count[character])
            # Set count[character] = 0 to denote that we do not need to 
            # write 'character' to our answer anymore
            count[character] = 0
            
        # Write all remaining characters that wasnt in order string but in the input string
        # to the end of the result.
        for character in count:
            result.append(character * count[character])
            
        return "".join(result)
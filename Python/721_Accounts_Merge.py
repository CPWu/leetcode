class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # Time: O(NklogNK), Space: O(NK)
        # There is also a Disjoint Set Union approach
        email_to_name = dict()
        adj_lists = collections.defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                adj_lists[account[1]].add(email)
                adj_lists[email].add(account[1])
                email_to_name[email] = account[0]
                
        visited = set()
        result = []
        for email in adj_lists:
            if email in visited:
                continue
            visited.add(email)
            stack = [email]
            emails = []
            while stack:
                email = stack.pop()
                emails.append(email)
                for alt_email in adj_lists[email]:
                    if alt_email in visited: continue
                    visited.add(alt_email)
                    stack.append(alt_email)
            result.append([email_to_name[email]] + sorted(emails))
    
        return result
        
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        p = path.split("/")
        p = [a for a in p if a != ""]

        stack = []

        for a in p:
            if a == ".":
                continue
            elif a == "..":
                if stack :
                    stack.pop()
            else:
                stack.append(a)

        return "/" + "/".join(stack)
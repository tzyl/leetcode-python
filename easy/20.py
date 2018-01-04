class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_parentheses = ("(", "{", "[")
        close_parentheses = (")", "}", "]")
        map_close_to_open = {c: o for c, o in zip(
            close_parentheses, open_parentheses)}
        stack = []
        for c in s:
            if c in open_parentheses:
                stack.append(c)
            elif c in close_parentheses:
                if not stack or map_close_to_open[c] != stack.pop():
                    return False
        return True if not stack else False

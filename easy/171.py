class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i, c in enumerate(s[::-1]):
            result += (ord(c) - ord("A") + 1) * 26 ** i
        return result

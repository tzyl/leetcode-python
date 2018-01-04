class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        negative = False
        i = 0
        # Check for optional sign character.
        if s[0] == "-":
            negative = True
            i += 1
        elif s[0] == "+":
            i += 1
        result = 0
        while i < len(s) and ord("0") <= ord(s[i]) <= ord("9"):
            result = result * 10 + ord(s[i]) - ord("0")
            i += 1
        if negative:
            result *= -1
        # Check if we overflowed.
        result = max(min(result, 2147483647), -2147483648)
        return result

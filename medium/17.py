from itertools import product


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        digits_to_letters = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        return list(map(lambda x: "".join(c for c in x), product(*(digits_to_letters[int(digit)] for digit in digits))))

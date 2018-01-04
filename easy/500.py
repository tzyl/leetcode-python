class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        possible_words = [word for word in words if any(all(c.lower() in row for c in word) for row in rows)]
        return possible_words

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        int_to_numeral = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        descending = sorted(int_to_numeral, reverse=True)
        numeral = ""
        for x in descending:
            numeral += num // x * int_to_numeral[x]
            num = num % x
        return numeral

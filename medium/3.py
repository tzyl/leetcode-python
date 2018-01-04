class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        j = 0
        in_substring = 0
        for i in xrange(len(s)):
            while j < len(s) and not in_substring & (1 << ord(s[j])):
                in_substring |= (1 << ord(s[j]))
                j += 1
            longest = max(longest, j - i)
            in_substring &= ~(1 << ord(s[i]))
        return longest


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abcabcbb")

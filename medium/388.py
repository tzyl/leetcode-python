class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        longest = 0
        lines = input.split("\n")
        lengths = []
        for line in lines:
            indents = line.rfind("\t") + 1
            # Update what level we are indented to.
            while len(lengths) > indents:
                lengths.pop()
            # Add length of this path to stack
            prev = lengths[-1] if lengths else -1
            lengths.append(prev + 1 + len(line) - indents)
            # Check if this is a file path.
            if "." in line:
                longest = max(longest, lengths[-1])
        return longest


if __name__ == '__main__':
    # test = "a\n\tb.txt\na2\n\tb2.txt"
    test = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print Solution().lengthLongestPath(test)
